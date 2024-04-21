
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Avaliacao, Comentario
from Livro.models import Livro
from Usuario.models import Usuario
from .serializer import (
    LivroSerializer,
    UsuarioSerializer,
    AvaliacaoSerializer,
    ComentarioSerializer
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication


class AvaliacaoCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def post(self, request):
            livro_avaliado = request.data.get('livro_avaliado')
            livro_avaliado = Livro.objects.filter(id = livro_avaliado)
            livro_avaliado = livro_avaliado.first()
            usuario_avaliando = request.user
            nota = request.data.get('nota')
            descricao = request.data.get('descricao')
            
            avaliacao = Avaliacao.objects.create(livro_avaliado=livro_avaliado,usuario_avaliando=usuario_avaliando,nota=nota,descricao=descricao)  
            avaliacao.save()
            return Response({'status': 201, 'msg': 'registered successfully'})
    
    def delete(self, request, avaliacao_id):
        try:
            avaliacao = Avaliacao.objects.get(id=avaliacao_id)
            avaliacao.delete()
            return Response({'status': 204, 'msg': 'deleted successfully'})
        except Avaliacao.DoesNotExist:
            return Response({'status': 404, 'msg': 'Avaliacao not found'})


class ComentarioCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def post(self, request):
            avaliacao_comentada = request.data.get('avaliacao_comentada')
            avaliacao_comentada = Avaliacao.objects.filter(id = avaliacao_comentada)
            avaliacao_comentada = avaliacao_comentada.first()
            usuario_comentando = request.user
            descricao = request.data.get('descricao')
            
            comentario = Comentario.objects.create(avaliacao_comentada=avaliacao_comentada,usuario_comentando=usuario_comentando,descricao=descricao)  
            comentario.save()
            return Response({'status': 201, 'msg': 'registered successfully'})
    
    def delete(self, request, comentario_id):
        try:
            comentario = Comentario.objects.get(id=comentario_id)
            comentario.delete()
            return Response({'status': 204, 'msg': 'deleted successfully'})
        except Comentario.DoesNotExist:
            return Response({'status': 404, 'msg': 'Comentario not found'})


class AvaliacaoListAPIView(APIView):
    def get(self, request, livro_id):
        avaliacoes = Avaliacao.objects.filter(livro_avaliado_id=livro_id)
        
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)
    

class ComentariosListAPIView(APIView):
     def get(self, request, avaliacao_id):
        comentarios = Comentario.objects.filter(avaliacao_comentada_id=avaliacao_id)
        
        serializer = ComentarioSerializer(comentarios, many=True)
        return Response(serializer.data)