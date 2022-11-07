from django.shortcuts import render
from django.views.generic import View

class HomeView(View):
    
    def get(self, request):
        return render(request, 'base.html')

class Handler404(View):

    def get(self, request, *args, **kwargs):
        return render(request,'erros/erro_404.html')

class Handler500(View):

    def get(self, request, *args, **kwargs):
        return render(request,'erros/erro_500.html')
    