from django.forms import ValidationError
from django.views.generic import TemplateView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from perfil.models import PerfilUsuario
from perfil.forms import EditarPerfilForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from perfil.validators import validar_email_institucional_aluno, validar_email_institucional_professor, validar_tamanho_avatar, validar_tipo_avatar


class PerfilView(LoginRequiredMixin, TemplateView):
    template_name = 'perfil/perfil.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['perfil_usuario'] = PerfilUsuario.objects.filter(usuario=self.request.user).first()
        return context


class EditarPerfilView(LoginRequiredMixin, UpdateView):
    model = PerfilUsuario
    form_class = EditarPerfilForm
    template_name = 'perfil/editar_perfil.html'
    success_url = reverse_lazy('editar_perfil')
    
    def get_object(self):
        """Garante que o usuário só edite o próprio perfil"""
        return self.request.user.perfil
    
    
    def form_valid(self, form):
        """Lógica customizada quando form é válido"""
        # Salva o form primeiro
        email_institucional = form.cleaned_data.get('email_institucional')
        
        avatar = form.cleaned_data.get('avatar')
        # Valida o avatar se fornecido
        if avatar:
            try:
                validar_tamanho_avatar(avatar)
                validar_tipo_avatar(avatar)
            except ValidationError as e:
                messages.error(
                    self.request,
                    f"❌ Erro ao atualizar foto de perfil. {str(e)}"
                )
                return super().form_invalid(form)
            
        # Mensagens customizadas baseadas no email institucional
        if email_institucional:
            if validar_email_institucional_professor(email_institucional):
                messages.success(
                    self.request,
                    "🎓 Perfil atualizado! Email institucional reconhecido como professor."
                )
            elif validar_email_institucional_aluno(email_institucional):
                messages.success(
                    self.request,
                    "🎒 Perfil atualizado! Email institucional reconhecido como aluno."
                )
        else:
            messages.info(
                self.request,
                "📝 Perfil atualizado! Você pode adicionar um email institucional depois."
            )

        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Lógica customizada quando form é inválido"""
        

        messages.error(
            self.request,
            "❌ Erro ao atualizar o perfil. Email institucional inválido."
        )

        return super().form_invalid(form)

    

class ExcluirPerfilView(LoginRequiredMixin, View):
    
    def post(self, request, *args, **kwargs):
        perfil = request.user.perfil
        # Marca o usuário como deletado
        perfil.usuario.delete()
        perfil.delete()

        # Desloga o usuário
        logout(request)
        messages.warning(
            request,
            'Seu perfil foi excluído. Se desejar, entre em contato com o suporte para reativação.'
        )
        return redirect('login')