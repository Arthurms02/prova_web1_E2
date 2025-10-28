from django import template
from django.templatetags.static import static

register = template.Library()

@register.simple_tag
def perfil_campo(usuario, campo, default=''):
    """
    Retorna campo do perfil do usuário ou valor padrão
    
    Uso no template:
    {% perfil_campo user 'email_institucional' 'Digite seu email institucional' %}
    """
    try:
        # Verifica se o usuário tem perfil
        if hasattr(usuario, 'perfil') and usuario.perfil:
            valor = getattr(usuario.perfil, campo, None)
            
            # Se o valor existir e não for vazio, retorna ele
            if valor:
                return valor
            
            # Se não, retorna o default
            return default
        
        # Se não tem perfil, retorna default
        return default
        
    except Exception:
        # Em caso de erro, retorna default
        return default


@register.simple_tag
def perfil_campo_formatado(usuario, campo, default='', formato=None):
    """
    Retorna campo do perfil formatado (para datas, telefones, etc.)
    
    Uso no template:
    {% perfil_campo_formatado user 'data_nascimento' '' 'd/m/Y' %}
    """
    try:
        if hasattr(usuario, 'perfil') and usuario.perfil:
            valor = getattr(usuario.perfil, campo, None)
            
            if valor:
                # Para datas
                if formato and hasattr(valor, 'strftime'):
                    return valor.strftime(formato)
                
                # Para outros campos
                return valor
            
            return default
        
        return default
        
    except Exception:
        return default
