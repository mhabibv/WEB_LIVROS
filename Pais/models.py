from django.db import models

class Paises(models.Model):
    pais = models.CharField(max_length=30)


    def __str__(self):
        return self.pais