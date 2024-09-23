from django.urls import path
from . import views


app_name = "biblioteca"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("cadastro/", views.CadastroView.as_view(), name="cadastro"),
]

