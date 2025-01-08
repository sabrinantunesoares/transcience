# forms.py
from django import forms
from .models import Artigo

class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = ['titulo', 'palavras_chave', 'link', 'ano_id', 'relevancia_id']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Título do artigo'}),
            'palavras_chave': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Palavras-chave, separadas por vírgula'}),
            'link': forms.URLInput(attrs={'class': 'form-input', 'placeholder': 'Link do artigo'}),
            'ano_id': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Ano de publicação'}),
            'relevancia_id': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'titulo': 'Título',
            'palavras_chave': 'Palavras-chave',
            'link': 'Link',
            'ano_id': 'Ano',
            'relevancia_id': 'Relevância',
        }
