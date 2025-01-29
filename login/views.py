from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
import re
from django.contrib.auth import logout as logout_django
from biblioteca.models import Artigo, Favorito, Relevancia, Ano, PalavraChave, Sexualidade, Usuarios
from biblioteca.models import Artigo



def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
        
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        
        if len(senha) < 8:
            return HttpResponse('A senha deve ter no mínimo 8 caracteres.')
        
        if not re.search(r'[A-Z]', senha):  
            return HttpResponse('A senha deve conter pelo menos uma letra maiúscula.')
        if not re.search(r'\d', senha):  
            return HttpResponse('A senha deve conter pelo menos um número.')
        if not re.search(r'[^a-zA-Z0-9]', senha):  
            return HttpResponse('A senha deve conter pelo menos um caractere especial.')
       
        if User.objects.filter(username=username).exists():
            return HttpResponse('Já existe um usuário com esse username')
        
        if User.objects.filter(email=email).exists():
            return HttpResponse('Já existe um usuário com esse e-mail.')
    
       
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return HttpResponse('Usuário cadastrado com sucesso')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

       
        user = authenticate(username=username, password=senha)

        if user is not None:
           
            login_django(request, user)
           
            return redirect('biblioteca:index') 
        else:
            
            return HttpResponse('Email ou senha inválidos')
        


def logout(request):
    logout_django (request)
    return redirect('login')

@login_required(login_url="/auth/login/")    
def plataforma(request):
    if request.user.is_authenticated:
        return HttpResponse('plataforma')
    

@login_required(login_url="/auth/login/")

def novoArtigo(request):
    if request.method == "GET":
        relevancias = Relevancia.objects.all()
        anos = Ano.objects.all()
        palavras_chave = PalavraChave.objects.all()
        return render(request, 'biblioteca/cadastro_artigo.html', {
            'relevancias': relevancias,
            'anos': anos,
            'palavras_chave': palavras_chave
        })
    else:
        try:
           
            titulo = request.POST.get('titulo')
            link = request.POST.get('link')
            autor = request.POST.get('autor')
            relevancia_id = request.POST.get('relevancia_id')
            ano_id = request.POST.get('ano_id')
            palavras_chave_ids = request.POST.getlist('palavras_chave')  
            usuario_id = request.user.id

            
            relevancia = Relevancia.objects.get(id=relevancia_id)
            ano = Ano.objects.get(id=ano_id)
            palavras_chave = PalavraChave.objects.filter(id__in=palavras_chave_ids)
            usuario = User.objects.get(id=usuario_id)

            
            artigo = Artigo.objects.create(
                titulo=titulo,
                link=link,
                autor=autor,
                relevancia_id=relevancia,
                ano_id=ano
            )

            
            artigo.palavras_chave.set(palavras_chave) 
            artigo.usuario.set([usuario])  

            return HttpResponse('Artigo cadastrado com sucesso')

        except Exception as e:
            return HttpResponse(f"Erro ao cadastrar artigo: {e}")


@login_required
def profile_view(request):
    return render(request, 'perfil.html', {'user': request.user})



def favoritar_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    favorito, created = Favorito.objects.get_or_create(usuario=request.user, artigo=artigo)

    if not created:  
        favorito.delete()

    return redirect('biblioteca:index')  