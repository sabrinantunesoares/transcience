from django.db import models

# Tabelas primárias

class Ano(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao
    
class Relevancia(models.Model):
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='biblioteca/images/relevancia/')

    def __str__(self):
        return self.descricao
    
class PalavraChave(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Idioma(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Autoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Genero(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao
    
class Vinculo(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao

class Sexualidade(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

# Tabelas secundária

class Usuarios(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    nascimento = models.DateField()
    senha = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)
    data_registro = models.DateField()
    instituicao = models.CharField(max_length=100, default="Escola")
    foto = models.ImageField(upload_to='biblioteca/images/perfil/', default='biblioteca/images/perfil/foto_perfil.png')

    vinculo = models.ForeignKey(Vinculo, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    sexualidade = models.ForeignKey(Sexualidade, on_delete=models.CASCADE)


    def __str__(self):
        return self.nome

class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    link = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)

    relevancia_id = models.ForeignKey(Relevancia, on_delete=models.CASCADE)
    ano_id = models.ForeignKey(Ano, on_delete=models.CASCADE)
    
    palavras_chave = models.ManyToManyField(PalavraChave, related_name='artigos')
    usuario = models.ManyToManyField(Usuarios, related_name='artigos')

    def __str__(self):
        return self.titulo


    titulo = models.CharField(max_length=200)
    link = models.CharField(max_length=255)
    

    def __str__(self):
        return self.titulo
    

class Favorito(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE)
    data_favorito = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.artigo}"
