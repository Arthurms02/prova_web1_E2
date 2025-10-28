from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from .models import Questao, Materia
from .forms import ResponderQuestaoForm, CreateQuestaoForm
from django.contrib import messages
from django.shortcuts import get_object_or_404 , redirect
from django.contrib.auth.mixins import LoginRequiredMixin


class CriarQuestaoView(LoginRequiredMixin, CreateView):
    model = Questao
    form_class = CreateQuestaoForm
    template_name = 'hometask/criar_questao.html'
    success_url = '/hometask/questoes/'

    def form_valid(self, form):
        form.instance.autor = self.request.user.perfil
        response = super().form_valid(form)
        messages.success(self.request, 'Questão criada com sucesso!')
        return response


class ListarQuestoesView(LoginRequiredMixin,ListView):
    """View para listar questões filtradas por matéria"""
    model = Questao
    template_name = 'hometask/listar_questao.html'
    context_object_name = 'questoes'
    paginate_by = 2
    
    def get_materia(self):
        """Retorna a matéria baseada no slug da URL"""
        if not hasattr(self, '_materia'):
            materia_slug = self.kwargs.get('materia_slug')
            if materia_slug:
                self._materia = get_object_or_404(Materia, slug=materia_slug)
            else:
                self._materia = None
        return self._materia
    
    def get_queryset(self):
        """Retorna questões da matéria específica"""
        queryset = Questao.objects.select_related('materia').order_by('-created_at')
        materia = self.get_materia()
        

        if materia:
            return queryset.filter(materia=materia)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        """Adiciona dados extras ao contexto"""
        context = super().get_context_data(**kwargs)
        materia = self.get_materia()
        
        if materia:
            context['materia_atual'] = materia
            context['titulo_pagina'] = f"Banco de Questões - {materia.nome}"
        else:
            context['materia_atual'] = None
            context['titulo_pagina'] = 'Banco de Questões - Todas as Matérias'
        
        context['materias_disponiveis'] = Materia.objects.all()

        return context
    

class QuestaoDetailView(LoginRequiredMixin,DetailView):
    model = Questao
    template_name = 'hometask/responder_questao.html'
    context_object_name = 'questao'
    paginate_by = 1


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        questao_atual = self.get_object()
        
        # ✅ CORREÇÃO: Navegação baseada em data de criação
        materia_slug = self.kwargs.get('materia_slug')
        
        if materia_slug:
            materia = get_object_or_404(Materia, slug=materia_slug)
            
            # Próxima questão (mais nova que a atual)
            proxima_questao = Questao.objects.filter(
                materia=materia,
                created_at__gt=questao_atual.created_at
            ).order_by('created_at').first()
            
            # Questão anterior (mais antiga que a atual)
            anterior_questao = Questao.objects.filter(
                materia=materia,
                created_at__lt=questao_atual.created_at
            ).order_by('-created_at').first()
            
            context['materia'] = materia
            context['proxima_questao'] = proxima_questao
            context['anterior_questao'] = anterior_questao
        
        context['form'] = ResponderQuestaoForm(questao=self.object)
        return context

    def post(self, request, *args, **kwargs):
        """
        Lida com a submissão do formulário de resposta via POST.
        """
        questao = self.get_object()
        form = ResponderQuestaoForm(request.POST, questao=questao)

        if form.is_valid():
            resposta_selecionada = form.cleaned_data['resposta']
            
            if resposta_selecionada == questao.resposta_correta:
                messages.success(request, "🎉 Parabéns, você acertou!")
            else:
                texto_correto = questao.resposta_correta_texto()
                messages.error(request, f"❌ Resposta incorreta. A alternativa correta era: '{texto_correto}'")
        else:

            messages.error(request, "⚠️ Você precisa selecionar uma alternativa.")


        return redirect('hometask:detalhe_questao', **self.kwargs)
