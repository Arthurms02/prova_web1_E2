from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    # Campos mostrados na lista
    list_display = ('email', 'first_name', 'last_name', 'is_professor')
    
    # Campos para filtrar
    list_filter = ('is_professor', 'is_staff')
    
    # Campo de busca
    search_fields = ('email', 'first_name', 'last_name')
    
    # Organização dos campos no formulário de edição
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'is_professor')}),
        ('Permissões', {'fields': ( 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', )}),
    )
    
    # Campos para criação de novo usuário
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'is_professor', 'password1', 'password2'),
        }),
    )
    
    # Define que o email é usado para ordenação
    ordering = ('email',)