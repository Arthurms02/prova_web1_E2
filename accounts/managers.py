from django.contrib.auth.base_user import BaseUserManager
from django.db import models



class UsuarioQuerySet(models.QuerySet):
    """
    QuerySet customizado para o modelo de usuário
    """
    def actives(self):
        """
        Retorna apenas usuários ativos
        """
        return self.filter(user_deletado=False)
    
    


class UsuarioManager(models.Manager):
    """
    Manager customizado para o modelo de usuário
    """
    def get_queryset(self):
        return UsuarioQuerySet(self.model, using=self._db)
    
    def actives(self):
        """
        Retorna apenas usuários ativos
        """
        return self.get_queryset().actives()
    
    def with_deleted(self):
        """
        Retorna todos os usuários, incluindo os deletados
        """
        return self.all()
    


class CustomUserManager(BaseUserManager):
    """
    Manager customizado para criar usuários
    """
    
    def _create_user(self, email, password, **extra_fields):
        """
        Método base para criar usuários
        """
        if not email:
            raise ValueError('O email é obrigatório')
        
        # Normaliza o email
        email = self.normalize_email(email)
        
        # Cria o usuário
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Faz o hash da senha automaticamente
        user.save(using=self._db)
        
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        """
        Cria um usuário comum.
        O tipo será determinado pelo campo 'tipo' passado em extra_fields
        """
        # Valores padrão para usuário comum
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_professor', False)
        
        
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password=None, **extra_fields):
        """
        Cria um superusuário
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self._create_user(email, password, **extra_fields)