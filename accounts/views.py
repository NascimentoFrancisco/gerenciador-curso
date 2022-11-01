from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.

class LoginUser(LoginView):

    model = CustomUser
    template_name = 'accounts/login.html'

class LogoutUser(LogoutView):

    template_name = 'base.html'

class CustomUserCreate(CreateView):

    model = CustomUser
    template_name = 'accounts/create.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('accounts:login_user')

    def form_valid(self, form):
        messages.info(
            self.request, "Cadastro realizado com sucesso! Faça seu login."
        )
        return super().form_valid(form)