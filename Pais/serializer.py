from rest_framework import serializers
from .models import Paises


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paises
        fields = '__all__'