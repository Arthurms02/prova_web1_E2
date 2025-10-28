from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from perfil.models import PerfilUsuario
from perfil.forms import EditarPerfilForm


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
        self.object = form.save()
        
        # Mensagens customizadas baseadas no email
        if form.cleaned_data.get('email_institucional'):
            messages.success(
                self.request,
                "✅ Perfil atualizado! Email institucional foi validado e salvo."
            )
        else:
            messages.info(
                self.request,
                "📝 Perfil atualizado! Você pode adicionar um email institucional depois."
            )
        
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context