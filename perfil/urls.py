from django.urls import path
from perfil.views import PerfilView, EditarPerfilView, ExcluirPerfilView


urlpatterns = [
    path('', PerfilView.as_view(), name='perfil'),
    path('editar/', EditarPerfilView.as_view(), name='editar_perfil'),
    path('excluir/', ExcluirPerfilView.as_view(), name='excluir_perfil'),
]