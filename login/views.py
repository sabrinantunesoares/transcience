from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
import re
from django.contrib.auth import logout as logout_django

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