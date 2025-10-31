from django.db import models
from perfil.models import PerfilUsuario
import uuid
from hometask.validators import upload_path_complemento


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Materia(BaseModel):
    """Modelo para representar uma matéria na questão."""
    nome = models.CharField(max_length=100, unique=True)

    slug = models.SlugField(unique=True, null=False, blank=False)

    def __str__(self):
        return self.nome


class Questao(BaseModel):
    """Modelo para representar uma questão de múltipla escolha."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    enunciado = models.TextField()
    complemento = models.ImageField(upload_to=upload_path_complemento, null=True, blank=True)
    alternativa_a = models.CharField(max_length=500, null=True, blank=True)
    alternativa_b = models.CharField(max_length=500, null=True, blank=True)
    alternativa_c = models.CharField(max_length=500, null=True, blank=True)
    alternativa_d = models.CharField(max_length=500, null=True, blank=True)
    alternativa_e = models.CharField(max_length=500, null=True, blank=True)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='questoes')
    autor = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE, related_name='questoes_criadas')

    OPCOES_RESPOSTA = [
        ('A', 'Alternativa A'),
        ('B', 'Alternativa B'),
        ('C', 'Alternativa C'),
        ('D', 'Alternativa D'),
        ('E', 'Alternativa E'),
    ]
    resposta_correta = models.CharField(max_length=1, choices=OPCOES_RESPOSTA)

    def get_alternativas(self):
        """Retorna uma lista de tuplas (letra, texto) das alternativas disponíveis."""
        todas = [
            ("A", self.alternativa_a),
            ("B", self.alternativa_b),
            ("C", self.alternativa_c),
            ("D", self.alternativa_d),
            ("E", self.alternativa_e),
        ]
        
        return [(letra, texto) for letra, texto in todas if texto]
    
    def resposta_correta_texto(self):
        """Retorna o texto da alternativa correta."""
        
        return self.resposta_correta

    def __str__(self):
        return self.enunciado[:50] + ('...' if len(self.enunciado) > 50 else '')


