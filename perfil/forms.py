from django import forms
from perfil.models import PerfilUsuario



class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ['bio', 'avatar', 'email_institucional', 'telefone', 'data_nascimento']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'email_institucional': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'user@unifip.br'
            }),
        }
        labels = {
            'bio': 'Biografia',
            'email_institucional': 'Email Institucional',
            'telefone': 'Telefone',
            'data_nascimento': 'Data de Nascimento',
        }
    

