from rest_framework import serializers
from .models import Generos, Genero_Livro, Genero_Autor


class GenerosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generos
        fields = ['nome_Genero']



class GeneroLivroSerializer(serializers.ModelSerializer):
    Genero = GenerosSerializer()

    class Meta:
        model = Genero_Livro
        fields = ['Genero']

class GeneroAutorSerializer(serializers.ModelSerializer):
    Genero = GenerosSerializer()

    class Meta:
        model = Genero_Autor
        fields = ['Genero']



