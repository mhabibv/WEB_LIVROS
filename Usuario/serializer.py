from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Usuario
from Pais.serializer import PaisSerializer


class UsuarioSerializer(serializers.ModelSerializer):

    Pais_id = PaisSerializer()

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'nome', 'telefone', 'Pais_id')