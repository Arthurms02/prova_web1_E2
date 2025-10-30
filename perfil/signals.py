# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from perfil.models import PerfilUsuario



# @receiver(post_save, sender=PerfilUsuario)
# def definir_avatar_padrao(sender, instance, created, **kwargs):
#     """Define um avatar padrão se nenhum for fornecido"""
#     if created and not instance.avatar:
#         first_letter = instance.usuario.first_name[0].upper() if instance.usuario.first_name else 'U'
#         instance.avatar = f'images/perfil_80X80/{first_letter}_80.png'
#         instance.save()