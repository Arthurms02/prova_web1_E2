from django import forms
from perfil.models import PerfilUsuario
from perfil.validators import validar_email_institucional


class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ['bio', 'avatar', 'email_institucional', 'telefone', 'data_nascimento']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'foto_perfil': forms.FileInput(attrs={'class': 'form-control'}),
            'email_institucional': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'professor@unifip.br'
            }),
        }
        labels = {
            'bio': 'Biografia',
            'email_institucional': 'Email Institucional',
            'telefone': 'Telefone',
            'data_nascimento': 'Data de Nascimento',
        }
    
    def clean_email_institucional(self):
        """Valida o email institucional usando o método do modelo PerfilUsuario"""
        email = self.cleaned_data.get('email_institucional')

        if email:

            valido, resultado = validar_email_institucional(email)

            if not valido:
                raise forms.ValidationError(resultado)

        return email