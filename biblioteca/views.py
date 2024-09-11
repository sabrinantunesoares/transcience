from django.shortcuts import render
from django.views import generic
from .models import Artigo

class IndexView(generic.ListView):
    template_name = "biblioteca/index.html"
    context_object_name = "artigos"

    def get_queryset(self):
        return Artigo.objects.all()

