from django.db import models

from Livro.models import Livro
from Autor.models import Autor


class Generos(models.Model):

    nome_Genero = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nome_Genero

class Genero_Autor(models.Model):
    Genero = models.ForeignKey(Generos, on_delete=models.CASCADE)
    Autor_Genero = models.ForeignKey(Autor, on_delete=models.CASCADE)


class Genero_Livro(models.Model):
    Genero = models.ForeignKey(Generos, on_delete=models.CASCADE)
    Livro_Genero = models.ForeignKey(Livro, on_delete = models.CASCADE)

