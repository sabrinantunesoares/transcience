from django.shortcuts import render
from django.views import generic
from .models import Artigo

class IndexView(generic.ListView):
    template_name = "biblioteca/index.html"
    context_object_name = "artigos"

    def get_queryset(self):
        return Artigo.objects.all()

class HomeView(generic.ListView):
    template_name = "biblioteca/home.html"
    context_object_name = "biblioteca"

    def get_queryset(self):
        return Artigo.objects.all()

class CadastroView(generic.ListView):
    template_name = "biblioteca/cadastro.html"
    context_object_name = "biblioteca"

    def get_queryset(self):
        return Artigo.objects.all()
    
class LoginView(generic.ListView):
    template_name = "biblioteca/login.html"
    context_object_name = "biblioteca"

    def get_queryset(self):
        return Artigo.objects.all()
    
class Cadastro_artigoView(generic.ListView):
    template_name = "biblioteca/cadastro_artigo.html"
    context_object_name = "biblioteca"

    def get_queryset(self):
        return Artigo.objects.all()
    
class PerfilView(generic.ListView):
    template_name = "biblioteca/perfil.html"
    context_object_name = "biblioteca"

    def get_queryset(self):
        return Artigo.objects.all()