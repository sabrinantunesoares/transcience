from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
import re
from django.contrib.auth import logout as logout_django
from biblioteca.models import Artigo, Relevancia, Ano, PalavraChave, Sexualidade, Usuarios
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
        
        if not re.search(r'[A-Z]', senha):  # Verifica letra maiúscula
            return HttpResponse('A senha deve conter pelo menos uma letra maiúscula.')
        if not re.search(r'\d', senha):  # Verifica número
            return HttpResponse('A senha deve conter pelo menos um número.')
        if not re.search(r'[^a-zA-Z0-9]', senha):  # Verifica caractere especial
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
        titulo = request.POST.get('titulo')
        link = request.POST.get('link')
        autor = request.POST.get('autor')
        relevancia_id = request.POST.get('relevancia_id')
        ano_id = request.POST.get('ano_id')
        palavras_chave_ids = request.POST.getlist('palavras_chave') 
        usuario_id = request.user.id  

        try:
            
            relevancia = Relevancia.objects.get(id=relevancia_id)
            ano = Ano.objects.get(id=ano_id)
            palavras_chave = PalavraChave.objects.filter(id__in=palavras_chave_ids)
            usuario = Usuarios.objects.get(id=usuario_id)

         
            artigo = Artigo.objects.create(
                titulo=titulo,
                link=link,
                autor=autor,
                relevancia_id=relevancia,
                ano_id=ano,
            )
        
            artigo.palavras_chave.set(palavras_chave)
            artigo.usuario.add(usuario)
            artigo.save()

            return HttpResponse('Artigo cadastrado com sucesso')

        except Exception as e:
            return HttpResponse(f"Erro ao cadastrar artigo: {e}")


def pesquisar_artigos(request):
    busca = request.GET.get('q')  # Captura o termo de pesquisa do parâmetro GET 'q'

    if busca:
        # Filtra os artigos que têm palavras-chave relacionadas ao termo de busca
        artigos = Artigo.objects.filter(palavras_chave__nome__icontains=busca)
    else:
        # Caso não haja pesquisa, retorna todos os artigos
        artigos = Artigo.objects.all()

    return render(request, 'index.html', {'artigos': artigos})  # Envia os artigos encontrados para o template

def novaSexualidade(request):
    if request.method == "GET":
        return render(request, 'index.html')
    elif request.method == "POST":
        # Capturar o dado enviado pelo formulário
        nome = request.POST.get('nome')

        # Validar o campo (opcional)
        if not nome:
            return HttpResponse('Erro: O campo sexualidade é obrigatório.', status=400)

        # Criar e salvar o objeto no banco de dados
        nova_sexualidade = Sexualidade.objects.create(nome=nome)

        return HttpResponse('Sexualidade cadastrada com sucesso!')
