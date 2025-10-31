from django.db import models
from django.templatetags.static import static
from accounts.models import Usuario
from perfil.validators import validar_tamanho_avatar, validar_tipo_avatar, upload_path_avatar,validar_email_institucional, validar_email_institucional_professor



class BaseModel(models.Model):
    """
    Modelo base abstrato para adicionar campos comuns a todos os modelos
    """
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    perfil_deletado = models.BooleanField(default=False, verbose_name='Perfil Deletado')

    class Meta:
        abstract = True

class PerfilUsuario(BaseModel):
    """
    Modelo para armazenar informações adicionais do usuário
    """
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='perfil')
    bio = models.TextField(blank=True, verbose_name='Biografia')
    avatar = models.ImageField(upload_to=upload_path_avatar, validators=[validar_tamanho_avatar, validar_tipo_avatar], blank=True, null=True, verbose_name='Avatar')
    telefone = models.CharField(max_length=15, blank=True, verbose_name='Telefone')
    data_nascimento = models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')
    # Email institucional do usuário
    email_institucional = models.EmailField(
        blank=True,
        null=True,
        default=None,
        verbose_name='Email Institucional',
        unique=True,
        validators=[validar_email_institucional]
    )

    class Meta:
        verbose_name = 'Perfil de Usuário'
        verbose_name_plural = 'Perfis de Usuários'

    def __str__(self):
        return f"Perfil de {self.usuario.nome_completo}"
    

    def delete(self):
        """
        Sobrescreve o método delete para marcar o perfil como deletado em vez de removê-lo do banco
        """
        self.perfil_deletado = True
        self.save()


    def save(self, *args, **kwargs):
        """
        Sobrescreve o método save para validar o email institucional antes de salvar
        """

        if self.email_institucional:
            if validar_email_institucional_professor(self.email_institucional):
                self.usuario.is_professor = True
                self.usuario.save()
            else:
                self.usuario.is_professor = False
                self.usuario.save()
        super().save(*args, **kwargs)

    def get_avatar_url(self):
        """Retorna a URL do avatar ou a imagem padrão se não houver avatar"""
        if self.avatar:
            return self.avatar.url
        else:
            first_letter = self.usuario.first_name[0].upper() if self.usuario.first_name else 'U'
            return static(f"perfil/images/perfil_80X80/{first_letter}_80.png")
    