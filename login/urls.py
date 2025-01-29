from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('novoArtigo/', views.novoArtigo, name='novoArtigo'),
    path('plataforma/', views.plataforma, name='plataforma'),
    path('profile_view/', views.profile_view, name='perfil'),
    path('favoritar/<int:artigo_id>/', views.favoritar_artigo, name='favoritar_artigo'),
]