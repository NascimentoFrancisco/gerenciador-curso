from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, ListView,View
from django.core.mail import send_mail
from django.conf import settings
from accounts.models import CustomUser

from .models import Aluno, CursoAluno
from curso.models import Curso
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

class CursoAlunoCreate(LoginRequiredMixin,CreateView):
    model = CursoAluno
    template_name = 'create.html'
    fields = ['curso']
    login_url = reverse_lazy('accounts:login_user')
    success_url = reverse_lazy('alunos:list_curso_aluno')

    def form_valid(self, form):
        try:
            aluno = Aluno.objects.get(user=self.request.user)
            form.instance.aluno = aluno
            curso = Curso.objects.get(id=form.data['curso'])
            curso_aluno = CursoAluno.objects.filter(curso__id = curso.id)
        
            if CursoAluno.objects.filter(aluno__id = aluno.id,curso__id=curso.id).exists():
                messages.warning(self.request,'Você já possui matrícula nesse curso!')
                return HttpResponseRedirect(reverse_lazy('alunos:list_curso_aluno'))

            elif len(curso_aluno) >= curso.numero_vagas:
                messages.warning(self.request,'Vagas esgotadas!')
                return HttpResponseRedirect(reverse_lazy('alunos:aluno_matricula'))

            elif timezone.now() < curso.inicio_matriculas:
                data = curso.inicio_matriculas.date().strftime("%d/%m/%Y")
                messages.info(self.request, 
                f"Perido de matrículas não iniciou ainda. Tal período se inicia {data}")
                return HttpResponseRedirect(reverse_lazy('alunos:aluno_matricula'))

            elif timezone.now() > curso.fim_matriculas:
                data = curso.fim_matriculas.date().strftime("%d/%m/%Y")
                messages.info(self.request, 
                f"Perido de matrículas já se encerrado. Tal período se encerrou {data}")
                return HttpResponseRedirect(reverse_lazy('alunos:aluno_matricula'))
            
            elif timezone.now() >= curso.inicio_matriculas and  timezone.now() <= curso.fim_matriculas:        
                messages.success(self.request, "Matrícula realizada com sucesso")
                form.save()
                """ send_mail('Mátricula',
                    f'Matrícula no curso {curso.titulo} foi realizada e confirmada com sucesso!',
                    settings.EMAIL_HOST_USER,['fmilk9049@gmail.com']) """
            else:
                messages.success(self.request, "Algo deu errado!")
                return HttpResponseRedirect(reverse_lazy('alunos:home_aluno'))

        except Aluno.DoesNotExist:
            
            messages.warning(self.request,'Complete seu cadstro!')
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
            messages.warning('Complete seu cadastro!')
            return HttpResponseRedirect(reverse_lazy('aluno:create_aluno'))
        try:
            queryset = CursoAluno.objects.filter(aluno=aluno)
        except CursoAluno.DoesNotExist:
            messages.warning('Você não possui matrícula em nenhum curso!')
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
    success_url = reverse_lazy('alunos:list_curso_aluno')
    template_name = 'cursos_aluno/delete.html'

    def get_success_url(self):
        messages.success(self.request, "Curso excluído com sucesso!")
        return reverse_lazy('alunos:list_curso_aluno')
