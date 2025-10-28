from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import Usuario
from perfil.models import PerfilUsuario
from django.templatetags.static import static


@receiver(post_save, sender=Usuario)
def criar_perfil_usuario(sender, instance, created, **kwargs):
    """Cria um perfil de usuário automaticamente quando um novo usuário é criado"""
    if created:
        PerfilUsuario.objects.create(usuario=instance)

