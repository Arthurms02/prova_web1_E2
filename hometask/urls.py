from django.urls import path
from hometask.views import ListarQuestoesView, CriarQuestaoView, QuestaoDetailView

# É uma excelente prática nomear suas URLs para evitar conflitos com outros apps
app_name = 'hometask'

urlpatterns = [
    # --- PÁGINAS DE LISTAGEM ---
    # Ambas as URLs apontam para a MESMA QuestaoListView.
    # A view saberá se deve filtrar ou não com base nos argumentos da URL.

    # 1. Lista TODAS as questões (Ex: /hometask/questoes/)
    path('questoes/', ListarQuestoesView.as_view(), name='lista_questoes'),

    # 2. Lista questões filtradas por matéria (Ex: /hometask/questoes/materia/matematica/)
    path('questoes/materia/<slug:materia_slug>/', ListarQuestoesView.as_view(), name='lista_questoes_por_materia'),


    # --- PÁGINA DE DETALHE / RESPONDER QUESTÃO ---
    # Usamos UMA ÚNICA URL para a página de detalhes.
    # Ela sempre inclui o slug da matéria, tornando-a mais informativa e robusta.

    # 3. Exibe UMA questão específica (Ex: /hometask/questoes/materia/matematica/uuid-da-questao/)
    path('questoes/materia/<slug:materia_slug>/<uuid:pk>/', QuestaoDetailView.as_view(), name='detalhe_questao'),
    

    # --- PÁGINA DE CRIAÇÃO ---
    # 4. Formulário para criar uma nova questão (Ex: /hometask/questoes/criar/)
    path('questoes/criar/', CriarQuestaoView.as_view(), name='criar_questao'),
]