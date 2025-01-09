from django.urls import path
from . import views


app_name = "biblioteca"
urlpatterns = [
    path("index/", views.IndexView.as_view(), name="index"),
    path("", views.HomeView.as_view(), name="home"),
    path("cadastro/", views.CadastroView.as_view(), name="cadastro"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("cadastro_artigo/", views.Cadastro_artigoView.as_view(), name="cadastro_artigo"),
    path('pesquisar/', views.pesquisar_artigos, name='pesquisar_artigos')
]

