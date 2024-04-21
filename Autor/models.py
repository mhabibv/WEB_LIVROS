from django.db import models


class Autor(models.Model):

    #foto
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    born_in = models.DateField()
    died_in = models.DateField(null = True, blank = True)
  


    def __str__(self):
        return self.nome
    







