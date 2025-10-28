from django import forms
from hometask.models import Questao

class CreateQuestaoForm(forms.ModelForm):
    class Meta:
        model = Questao
        fields = [
            'enunciado', 'complemento', 'alternativa_a', 'alternativa_b',
            'alternativa_c', 'alternativa_d', 'alternativa_e',
            'materia', 'resposta_correta'
        ]
        widgets = {
            'enunciado': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Digite o enunciado da questão'}),
            'complemento': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'alternativa_a': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alternativa A'}),
            'alternativa_b': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alternativa B'}),
            'alternativa_c': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alternativa C'}),
            'alternativa_d': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alternativa D'}),
            'alternativa_e': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alternativa E'}),
            'materia': forms.Select(attrs={'class': 'form-select'}),
            'resposta_correta': forms.Select(attrs={'class': 'form-select', 'id': 'resposta_correta', 'name': 'resposta_correta'}),
        }


class ResponderQuestaoForm(forms.Form):
    resposta = forms.ChoiceField(
        widget=forms.RadioSelect,
        required=True,
        label='Selecione a alternativa correta'
    )

    

    def __init__(self, *args, questao=None, **kwargs):
        super().__init__(*args, **kwargs)

        if questao:
            self.fields['resposta'].choices = questao.get_alternativas()
