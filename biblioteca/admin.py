from django.contrib import admin

from .models import Ano, Artigo, Genero, PalavraChave, Relevancia, Sexualidade, Usuarios, Vinculo, Idioma, Autoria, Favorito


admin.site.register(Artigo)
admin.site.register(Ano)
admin.site.register(Relevancia)
admin.site.register(PalavraChave)
admin.site.register(Idioma)
admin.site.register(Usuarios)
admin.site.register(Genero)
admin.site.register(Vinculo)
admin.site.register(Sexualidade)
admin.site.register(Autoria)
admin.site.register(Favorito)