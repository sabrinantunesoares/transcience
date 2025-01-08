from django.shortcuts import render
from django.views import generic
from .models import Artigo
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = "biblioteca/index.html"
    context_object_name = "artigos"
    login_url = '/auth/login/'  # Página de login para redirecionar se o usuário não estiver autenticado

    def get_queryset(self):
        return Artigo.objects.all()

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
    
def pesquisar_artigos(request):
    query = request.GET.get('q', '')
    if query:
        artigos = Artigo.objects.filter(palavras_chave__nome__icontains=query)
    else:
        artigos = Artigo.objects.all()

    return render(request, 'biblioteca/artigos.html', {'artigos': artigos})
