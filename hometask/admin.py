from django.contrib import admin
from .models import Questao, Materia


@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nome",)}


@admin.register(Questao)
class QuestaoAdmin(admin.ModelAdmin):
    list_display = ('enunciado', 'materia', 'resposta_correta')
    list_filter = ('materia',)
    search_fields = ('enunciado',)

