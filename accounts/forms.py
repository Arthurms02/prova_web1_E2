from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from accounts.models import Usuario


# Herda de UserCreationForm que já tem lógica para senhas
class RegistroForm(UserCreationForm):
    # Campo personalizado para nome completo
    nome = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',        # Classe CSS do Bootstrap
            'placeholder': 'Seu nome completo'  # Texto placeholder
        })
    )
    
    # Campo email com validação automática
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu Email'
        }),
        label='Email' 
    )
    
    
    # Campo senha 1 (herdado do UserCreationForm, mas personalizado)
    password1 = forms.CharField(
        label="Senha",  # Altera o label para português
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha'
        })
    )
    
    # Campo confirmação de senha
    password2 = forms.CharField(
        label="Confirme sua senha",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite a senha novamente'
        })
    )
    
    # Classe Meta configura o formulário
    class Meta:
        model = Usuario  # Modelo que este form representa
        fields = ['nome', 'email', 'password1', 'password2']  # Campos na ordem desejada
    
    # Método que salva os dados no banco
    def save(self, commit=True):
        # Cria o objeto usuário mas não salva ainda (commit=False)
        user = super().save(commit=False)
        
        # Processa o nome completo: divide em primeiro e último nome
        nome_completo = self.cleaned_data['nome'].split(' ', 1)
        user.first_name = nome_completo[0]  # Primeira parte = primeiro nome
        
        # Se tiver mais partes, pega o resto como último nome
        user.last_name = nome_completo[1] if len(nome_completo) > 1 else ''
        
        # Atribui os outros campos
        user.email = self.cleaned_data['email']

        
        # Salva no banco se commit=True
        if commit:
            user.save()
        return user
    
class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu Email'
        }),
        label='Email'
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha'
        }),
        label='Senha'
    )



