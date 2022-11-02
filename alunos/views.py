from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, ListView,View
from accounts.models import CustomUser

from .models import Aluno, CursoAluno
from .forms import AlunoCreateForm
# Create your views here.

class HomeAluno(LoginRequiredMixin,View):

    login_url = reverse_lazy('accounts:login_user')

    def get(self, request):

        try:
            Aluno.objects.get(user=self.request.user)
            return render(request, 'aluno/home_aluno.html')
        except Aluno.DoesNotExist:
            messages.warning(self.request,'Complete seu cadastro!')
            return HttpResponseRedirect(reverse_lazy('alunos:create_aluno'))

class AlunoCreate(LoginRequiredMixin,CreateView):

    model = Aluno
    form_class = AlunoCreateForm
    template_name = 'create.html'
    login_url = reverse_lazy('accounts:login_user')
    success_url = reverse_lazy('alunos:home_aluno')

    def form_valid(self, form):
        form.instance.user = CustomUser.objects.get(id=self.request.user.id)
        return super().form_valid(form)

class CursoAlunoCreate(LoginRequiredMixin,CreateView):#Melhorar o fluxo de craição de matricula
    model = CursoAluno
    template_name = 'create.html'
    fields = ['curso']
    login_url = reverse_lazy('alunos:home_aluno')
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        try:
            form.instance.aluno = Aluno.objects.get(user=self.request.user)
        except Aluno.DoesNotExist:
            messages.warning('Complete seu cadstro!')
            return HttpResponseRedirect(reverse_lazy('aluno:create_aluno'))
        return super().form_valid(form)


class CursoAlunoList(LoginRequiredMixin,ListView):

    """
    Essa view busca os cursos no qual o aluno logado está matriculado.
    """   
    template_name = 'cursos_aluno/list.html'
    login_url = reverse_lazy('accounts:login_user')

    def get_queryset(self):
        user = self.request.user

        try:
            aluno = Aluno.objects.get(user=user)
        except Aluno.DoesNotExist:
            messages.warning('Complete seu cadstro!')
            return HttpResponseRedirect(reverse_lazy('aluno:create_aluno'))
        try:
            queryset = CursoAluno.objects.filter(aluno=aluno)
        except CursoAluno.DoesNotExist:
            messages.warning('Você não está matriculado em nenhum curso!')
            return None

        return queryset

class CursoAlunoListPorCurso(LoginRequiredMixin,ListView):
    
    """
    Esse view busca as matriculas feitas em um determinaddo curso através de seu id passdo na url.
    """
    model = CursoAluno
    template_name = 'cursos_aluno/list_aluno_curso.html'
    login_url = reverse_lazy('accounts:login_user')

    def get_queryset(self):
        queryset = CursoAluno.objects.filter(curso__id=self.kwargs['pk'])
        return queryset

class CursoAlunoDelete(LoginRequiredMixin, DeleteView):
    model = CursoAluno
    login_url = reverse_lazy('accounts:login_user')
    success_url = reverse_lazy('cursos:list_curso_aluno')
    template_name = 'cursos_aluno/delete.html'

    def get_success_url(self):
        messages.success(self.request, "Curso excluído com sucesso!")
        return reverse_lazy('cursos:list_curso_aluno')
