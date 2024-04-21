
from rest_framework import generics
from .models import Autor
from .serializer import AutorSerializerDetaield,ListaAutoresSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Genero.models import Generos, Genero_Autor
from rest_framework.viewsets import ModelViewSet


class AutorModelViewSet(ModelViewSet):
    def create(self, request):
        nome = request.data.get('nome')
        descricao = request.data.get('descricao')
        descricao = request.data.get('descricao')
        born_in = request.data.get('born_in')
        died_in = request.data.get('died_in')
       
        generos_ids = request.data['genero_autor']
    
        autor = Autor.objects.create(nome=nome,descricao=descricao,born_in=born_in,died_in=died_in)  
        for genero_id in generos_ids:
            genero = Generos.objects.filter(id=genero_id).first()
            if genero:
                Genero_Autor.objects.create(Genero=genero, Autor_Genero=autor)


        return Response({'status': 201, 'msg': 'registered successfully'})
    


class AutorViewSet(ModelViewSet):
    def autor_detaield(self, request, pk=None):  
        if pk is not None:  
            try:
                autor = Autor.objects.get(pk=pk)
                serializer = AutorSerializerDetaield(autor)
                return Response({
                    'status': 302,
                    'Livro': serializer.data
                })
            except Autor.DoesNotExist:
                return Response({'status': 404, 'msg': 'Autor não encontrado'})
        else:
            return Response({'status': 404, 'msg': 'ID do Autor não fornecido'})
        

    def list_autor(self, request):
        autor = Autor.objects.all()
        serializer = ListaAutoresSerializer(autor, many=True)
        if len(serializer.data) > 0:
            return Response({
                'status': 302,
                'Livros': serializer.data
            })
        return Response({'status': 204, 'msg': 'No Content'})