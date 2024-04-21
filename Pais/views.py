from rest_framework.viewsets import ModelViewSet
from .models import Paises
from .serializer import PaisSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from Usuario.models import Usuario
from Usuario.serializer import UsuarioSerializer

class PaisModelViewSet(ModelViewSet):
    serializer_class = PaisSerializer
    queryset = Paises.objects.all()


    #Listar todos os paises:
    def list(self, request):
        p = Paises.objects.all()
        serial = PaisSerializer(p, many = True)
        if len(serial.data) > 0:
            return Response({
                'status': 302, 'Pais': serial.data
            })
        return Response({'status': 204, 'msg': 'No Content'})

    #Criar um pais
    def create(self, request):
        nome = request.data.get('pais')
        Paises.objects.create(pais = nome)
        return Response ({'status': 201, 'msg': 'registered successfully'})

    #Listar todos os Usuarios de um pais
    @action(methods=["get"], detail=False)
    def lista_usuarios_por_pais(self, request):
        pais = request.data.get('id')
        Us = Usuario.objects.filter(Pais_id = pais)
        serial = UsuarioSerializer(Us, many = True)
        if len(serial.data) > 0:
            return Response({
                'status': 302, 'Usuarios do Pais': serial.data
            })
        return Response({'status': 204, 'msg': 'No Content'})