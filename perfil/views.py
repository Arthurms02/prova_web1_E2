from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from perfil.models import PerfilUsuario
from perfil.forms import EditarPerfilForm
from perfil.validators import validar_email_institucional,validar_email_institucional_professor,validar_tipo_avatar,validar_tamanho_avatar



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
        form.save()
        email_institucional = form.cleaned_data.get('email_institucional')
        # Mensagens customizadas baseadas no email
        if email_institucional:
            messages.success(
                self.request,
                "✅ Perfil atualizado com sucesso! Email institucional registrado."
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
            "❌ Erro ao atualizar o perfil. Verifique os dados e tente novamente."
        )
        return super().form_invalid(form)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context