from rest_framework import generics
from .models import Livro
from .serializer import LivroSerializerDetaield, LivroSerializer
from Autor.models import Autor
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.http import JsonResponse
from Genero.models import Genero_Livro
from Genero.models import Generos

class LivroModelViewSet(ModelViewSet):
    def create(self, request):
        titulo = request.data.get('titulo')
        descricao = request.data.get('descricao')
        data_publicacao = request.data.get('data_publicacao')
        n_paginas = request.data.get('n_paginas')
        id_autor = request.data.get('id_autor')
        generos_ids = request.data['genero_livro']
        autor = Autor.objects.filter(id=id_autor)

        if not autor.exists():
            return Response({'status': 404, 'msg': 'Not Found.'})
        
        livro = Livro.objects.create(titulo=titulo,descricao=descricao,data_publicacao=data_publicacao,n_paginas=n_paginas,autor=autor.first())  
        for genero_id in generos_ids:
            genero = Generos.objects.filter(id=genero_id).first()
            if genero:
                Genero_Livro.objects.create(Genero=genero, Livro_Genero=livro)


        return Response({'status': 201, 'msg': 'registered successfully'})


class LivroViewSet(ModelViewSet):
    def list_detaield(self, request, pk=None):  
        if pk is not None:  
            try:
                livro = Livro.objects.get(pk=pk)
                serializer = LivroSerializerDetaield(livro)
                return Response({
                    'status': 302,
                    'Livro': serializer.data
                })
            except Livro.DoesNotExist:
                return Response({'status': 404, 'msg': 'Livro não encontrado'})
        else:
            return Response({'status': 404, 'msg': 'ID do livro não fornecido'})
        

    def list_livros(self, request):
        livros = Livro.objects.all()
        serializer = LivroSerializer(livros, many=True)
        if len(serializer.data) > 0:
            return Response({
                'status': 302,
                'Livros': serializer.data
            })
        return Response({'status': 204, 'msg': 'No Content'})
    

    def list_livro_autor(self, request, autor_id=None):
        if autor_id is not None:  
            try:
                autor = Autor.objects.get(pk=autor_id) 
                livros = Livro.objects.filter(autor=autor)  
                serializer = LivroSerializer(livros, many=True)
                if len(serializer.data) > 0:
                    return Response({
                        'status': 302,
                        'Livros': serializer.data
                    })
                else:
                    return Response({'status': 204, 'msg': 'No Content'})
            except Autor.DoesNotExist:
                return Response({'status': 404, 'msg': 'Autor não encontrado'})
        else:
            return Response({'status': 404, 'msg': 'ID do autor não fornecido'})
    

    
