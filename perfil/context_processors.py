from perfil.models import PerfilUsuario


def avatar_url(request):
    return {
        'AVATAR_URL': None if not request.user.is_authenticated else PerfilUsuario.objects.filter(usuario=request.user).first().get_avatar_url()
    }