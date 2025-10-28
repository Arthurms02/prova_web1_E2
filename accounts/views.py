from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib import messages
from accounts.models import Usuario
from accounts.forms import RegistroForm, EmailAuthenticationForm


class CustomLoginView(LoginView):
    form_class = EmailAuthenticationForm
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        messages.success(self.request, 'Login realizado com sucesso!')
        return super().form_valid(form)
    # def form_invalid(self, form):
    #     messages.error(self.request, 'Credenciais inválidas. Por favor, tente novamente.')
    #     return super().form_invalid(form)
    



class RegistroView(CreateView):
    model = Usuario 
    form_class = RegistroForm  
    template_name = 'accounts/register.html'  
    success_url = reverse_lazy('registro')

    
    # Método executado quando o formulário é válido
    def form_valid(self, form):

        response = super().form_valid(form)
        
        login(self.request, self.object)
        
        messages.success(
            self.request, 
            f'Cadastrado com sucesso! Bem-vindo(a), {self.object.first_name}!'
        )

        return response  
    
    # Método executado quando o formulário é inválido
    def form_invalid(self, form):

        response = super().form_invalid(form)

        messages.error(
            self.request,
            'Erro no cadastro. Verifique os dados informados.'
        )

        return response
    
    # Adiciona dados extras ao contexto do template
    def get_context_data(self, **kwargs):
        # Pega o contexto padrão da classe pai
        context = super().get_context_data(**kwargs)
        return context






    