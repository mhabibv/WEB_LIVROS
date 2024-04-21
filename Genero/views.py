from django.shortcuts import render

from rest_framework import generics
from .models import Generos
from .serializer import GenerosSerializer
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class GeneroModelViewSet(ViewSet):
    def create(self, request):
        nome_Genero = request.data.get('nome_Genero')
        genero = Generos.objects.create(nome_Genero=nome_Genero)
        serializer = GenerosSerializer(genero)
        return Response(serializer.data, status=201)
    
    def destroy(self, request, pk=None):
        try:
            genero = Generos.objects.get(pk=pk)
        except Generos.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        genero.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, pk):
        genero = Generos.objects.filter(id=pk)
        if not genero.exists():
            return Response({'status': 404, 'msg': 'Genero não encontrado'}, status = 404)
        genero = genero.first()
        nome_genero = request.data.get('nome_genero')
        if not nome_genero:
            return Response ({'status': 400, 'msg': 'Campo nome_genero é obrigatório'}, status = 400)
        genero.nome_Genero = nome_genero
        genero.save()
        return Response({'status': 200, 'msg': 'Alterado com SUCESSO'}, status = 200)