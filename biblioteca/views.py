from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from .models import Artigo, Favorito
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = "biblioteca/index.html"
    context_object_name = "artigos"
    login_url = '/auth/login/' 
    

    def get_queryset(self):
        query = self.request.GET.get('q')  
        if query:
            return Artigo.objects.filter(
                Q(titulo__icontains=query) | 
                Q(autor__icontains=query) |  
                Q(palavras_chave__nome__icontains=query)).distinct()
        return Artigo.objects.all() 
    
    def get_context_data(self, **kwargs):
        usuario_atual = self.request.user
        context = super(IndexView, self).get_context_data(**kwargs)
        favoritos = Favorito.objects.filter(usuario=usuario_atual).values_list('artigo_id')
        favoritos_ids = []
        for f in favoritos:
            if (f[0] not in favoritos_ids):
                favoritos_ids.append(f[0])
        context['favoritos'] = favoritos_ids
        return context

class ArtigoListView(LoginRequiredMixin, generic.ListView):
    model = Artigo
    template_name = 'biblioteca/minha_biblioteca.html'
    context_object_name = 'artigos'

    def get_queryset(self):
        return Artigo.objects.filter(usuario=self.request.user)

        
   
    

def lista_artigos(request):
    usuario_atual = request.user

    if usuario_atual.is_authenticated:
        artigos = usuario_atual.artigos.all()  # Aqui usamos o related_name 'artigos'
    else:
        artigos = []

    return render(request, 'biblioteca/lista_artigos.html', {'artigos': artigos})

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
    
class Minha_bibliotecaView(generic.ListView):
    template_name = "biblioteca/minha_biblioteca.html"
    context_object_name = "biblioteca"

    def get_queryset(self):
        return Artigo.objects.all()

def exemplo_view(request):
    if request.user.is_authenticated:
        usuario_logado = request.user  # Acessa o objeto User do usuário logado
        # Você pode acessar as informações do usuário, como:
        nome_usuario = usuario_logado.username
        email_usuario = usuario_logado.email
        # Ou qualquer outro campo associado ao modelo User

        # Exemplo de passar os dados para o template:
        return render(request, 'exemplo_template.html', {'usuario': usuario_logado})
    else:
        # Caso o usuário não esteja logado, você pode redirecioná-lo para a página de login
        return redirect('login')