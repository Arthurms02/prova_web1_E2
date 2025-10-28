from accounts.models import Usuario


def nome_usuario(request):
    return{
        'NOME_USUARIO': None if not request.user.is_authenticated else Usuario.objects.filter(id=request.user.id).first().nome_completo()
    }

