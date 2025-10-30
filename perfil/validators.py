import os
from uuid import uuid4
from django.core.exceptions import ValidationError
from django.contrib import messages
import re

def upload_path_avatar(instance, filename):
    """Gera um caminho único para o upload do avatar do usuário"""
    ext = filename.split('.')[-1]
    filename = f"{uuid4().hex}.{ext}"
    return os.path.join('avatars/', f'usuario_{instance.usuario.id}', filename)

def validar_tamanho_avatar(avatar):
    """Valida o tamanho do arquivo de avatar (máximo 2MB)"""
    limite_tamanho = 2 * 1024 * 1024  # 2MB
    if avatar.size > limite_tamanho:
        print('Tamanho do avatar excede o limite permitido.')
        raise ValidationError("O tamanho do avatar não pode exceder 2MB.")

def validar_tipo_avatar(avatar):
    """Valida o tipo do arquivo de avatar (permitidos: jpg, jpeg, png)"""
    ext_permitidas = ['jpg', 'jpeg', 'png']
    ext = avatar.name.split('.')[-1].lower()
    if ext not in ext_permitidas:
        print('Tipo de arquivo de avatar não permitido.')
        raise ValidationError("Tipo de arquivo não permitido. (permitidos: jpg, jpeg, png)")

def validar_email_institucional(email_institucional):
        """
        Valida se o email institucional pertence ao domínio correto
        """
        pattern = r'^[a-zA-Z0-9]+([._]?[a-zA-Z0-9]+)*@(aluno|professor)\.(unifip\.br|uepb\.br|ufcg\.br)$'
        if not re.match(pattern, email_institucional):
            raise ValidationError("Email institucional inválido.")
        return email_institucional

def validar_email_institucional_professor(email_institucional):
        """
        Valida se o email institucional pertence ao domínio correto para professores
        """
        pattern = r'^[a-zA-Z0-9]+([._]?[a-zA-Z0-9]+)*@(professor)\.(unifip\.br|uepb\.br|ufcg\.br)$'
        if not re.match(pattern, email_institucional):
            return False
        return True