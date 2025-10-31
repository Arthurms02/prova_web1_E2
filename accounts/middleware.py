from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages


class UsuarioDeletadoMiddleware:
    """
    Middleware para impedir que usuários deletados acessem o sistema
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Verifica se o usuário está autenticado
        if request.user.is_authenticated and hasattr(request.user, 'user_deletado') and request.user.user_deletado:
            # Desloga o usuário
            logout(request)
            # Adiciona uma mensagem informando que a conta foi deletada
            messages.warning(request, 'Sua conta foi deletada. Entre em contato com o suporte para mais informações.')
            # Redireciona para a página de login
            return redirect('login')
            
        
        response = self.get_response(request)
        return response