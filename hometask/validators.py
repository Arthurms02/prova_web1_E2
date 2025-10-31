import os
from uuid import uuid4

def upload_path_complemento(instance, filename):
    """Gera um caminho único para o upload do complemento da questão"""

    ext = filename.split('.')[-1]
    filename = f"{uuid4().hex}.{ext}"
    return os.path.join('complementos/', f'questao_{instance.created_at}', filename)