from rest_framework import serializers
from .models import Livro
from Genero.models import Genero_Livro
from Genero.serializer import GenerosSerializer,GeneroLivroSerializer
from Autor.serializer import ListaAutoresSerializer
from Autor.models import Autor

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['titulo','autor']


class LivroSerializerDetaield(serializers.ModelSerializer):
    generos_livro = serializers.SerializerMethodField()
    autor = serializers.SerializerMethodField()
    class Meta:
        model = Livro
        fields = ['titulo','descricao','data_publicacao','n_paginas','autor','generos_livro']

    def get_generos_livro(self, obj):
        generos_livro = Genero_Livro.objects.filter(Livro_Genero=obj.pk)
        nomes_generos = [genero_livro.Genero.nome_Genero for genero_livro in generos_livro]
        return nomes_generos
    
    def get_autor(self, obj):
        return obj.autor.nome