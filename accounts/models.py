from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager



class BaseModel(models.Model):
    """
    Modelo base abstrato para adicionar campos comuns a todos os modelos
    """
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        abstract = True 


class Usuario(BaseModel, AbstractBaseUser, PermissionsMixin):
    """
    Modelo de usuário customizado usando AbstractBaseUser e PermissionsMixin
    """
    
    # Campos obrigatórios que você deve definir
    email = models.EmailField(
        unique=True,
        verbose_name='Email'
    )
    
    first_name = models.CharField(
        max_length=150,
        verbose_name='Nome'
    )
    
    last_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Sobrenome'
    )
       
    # Campos que o AbstractUser tinha mas AbstractBaseUser não tem
    is_staff = models.BooleanField(
        default=False,
        verbose_name='Staff status',
        help_text='Identifica se o usuário pode acessar o site administrativo.'
    )

    is_professor = models.BooleanField(
        default=False,
        verbose_name='Professor status',
        help_text='Identifica se o usuário é um professor.'
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name='Active',
        help_text='Identifica se o usuário deve ser tratado como ativo, ao invés de deletar contas.'
    )
    
    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de cadastro'
    )
    
    # Conecta o manager customizado
    objects = CustomUserManager()
    
    # Define que o email será usado para login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['email']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} "
    
    def is_professor_user(self):
        """Retorna True se o usuário for um professor"""
        return self.is_professor
    
    def nome_completo(self):
        """Retorna o nome completo do usuário"""
        return f"{self.first_name} {self.last_name}".strip()
    



    

