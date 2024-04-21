from rest_framework import serializers
from .models import Autor
from Genero.serializer import GeneroAutorSerializer
from Genero.models import Genero_Autor


class ListaAutoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['nome']



class AutorSerializerDetaield(serializers.ModelSerializer):
    generos_autor = serializers.SerializerMethodField()
    class Meta:
        model = Autor
        fields = ['nome', 'descricao', 'born_in', 'died_in','generos_autor']

    def get_generos_autor(self, obj):
        generos_autor = Genero_Autor.objects.filter(Autor_Genero=obj.pk)
        nomes_generos = [Genero_Autor.Genero.nome_Genero for Genero_Autor in generos_autor]
        return nomes_generos