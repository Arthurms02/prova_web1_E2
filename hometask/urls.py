from django.urls import path
from hometask.views import ListarQuestoesView, CriarQuestaoView, QuestaoDetailView, EditarQuestaoView, ExcluirQuestaoView


app_name = 'hometask'

urlpatterns = [

    path('questoes/', ListarQuestoesView.as_view(), name='lista_questoes'),
    path('questoes/materia/<slug:materia_slug>/', ListarQuestoesView.as_view(), name='lista_questoes_por_materia'),
    path('questoes/materia/<slug:materia_slug>/<uuid:pk>/', QuestaoDetailView.as_view(), name='detalhe_questao'),
    path('questoes/materia/<slug:materia_slug>/<uuid:pk>/editar/', EditarQuestaoView.as_view(), name='editar_questao'),
    path('questoes/materia/<slug:materia_slug>/<uuid:pk>/excluir/', ExcluirQuestaoView.as_view(), name='excluir_questao'),
    path('questoes/criar/', CriarQuestaoView.as_view(), name='criar_questao'),
]