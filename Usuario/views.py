from rest_framework.viewsets import ModelViewSet
from .models import Usuario
from Pais.models import Paises
from Genero.models import Generos
from .serializer import UsuarioSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView




class RegisterView(APIView):

    def post(self, request):
        #Testa se o campo username é None ou se o username já está sendo utilizado
        username = request.data.get('username')
        if username is None:
            return Response({'status': 400, 'msg': 'O campo Username é obrigatório!'}, status = 400)
        user_exists = Usuario.objects.filter(username=username).exists()
        if user_exists:
            return Response({'status': 409, 'msg': 'Username já existente!'})
            
        #Testa se o campo password é None e se password é diferente  de confirm_password
        #Se forem iguais, criptografa a senha
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')
        if password is None:
            return Response({'status': 400, 'msg': 'O campo Password é obrigatório!'}, status = 400)
        
        if password != confirm_password:
            return Response({'status': 409, 'msg': 'As senhas precisam ser iguais'})

        hashed_password = make_password(password)
        
        #Testa se nome é None
        nome = request.data.get('nome')
        if nome is None:
            return Response({'status': 400, 'msg': 'O campo nome é obrigatório!'}, status = 400)

        #Testa se o campo email é None e se email já está sendo utilizado
        email = request.data.get('email')
        if email is None:
            return Response({'status': 400, 'msg': 'O campo email é obrigatório!'}, status = 400)
        email_exist = Usuario.objects.filter(email = email).exists()
        if email_exist:
            return Response({'status': 409, 'msg': 'Email já está em uso'})
        
        #Telefone é opcional, então não verifico nada
        tel = request.data.get('telefone')
        
        #Testa se pais é None e se aquele pais existe
        pais= request.data.get('pais')
        if pais is None:
            return Response({'status': 400, 'msg': 'O campo pais é obrigatório!'}, status = 400)
        pais = Paises.objects.filter(id = pais)
        if not pais.exists():
            return Response({'status': 404, 'msg': "Pais não encontrado"}, status= 404)
        
        #Descricao também é opcional, então não verifico nada
        descricao = request.data.get('descricao')
        
        #Testa se is private é None e se não é um boleano, se for, atribui falso a ele
        is_private = request.data.get('is_private')
        if is_private is None or not isinstance(is_private, bool):
            is_private = False

        
        #Recebe os generos como lista, se for algo diferente considera como None
        generos_favoritos = request.data.get('generos_favoritos', None)
        
        if generos_favoritos is not None:
            #Testa se é uma lista
            if not isinstance(generos_favoritos, list):
                return Response({'status': 400, 'msg': "O campo generos_favoritos deve ser uma lista."}, status=400)
    
            #Retira repetidos
            generos_favoritos = list(set(generos_favoritos))

            generos_id = []
            #Para cada genero, testa se ele existe. Se não, informa o erro
            for genero in generos_favoritos:
                genero = Generos.objects.filter(id = genero)
                if not genero.exists():
                    return Response ({'status': 404, 'msg': "Genero não encontrado"}, status= 404)
                generos_id.append(genero.first())    

        #Chegando aqui não tendo retornado nenhum erro, podemos fazer criar o Usuário
        usuario = Usuario.objects.create(
                    username=username, 
                    password=hashed_password, 
                    email=email, nome=nome, 
                    descricao=descricao,
                    telefone=tel, 
                    pais = pais.first(),
                    is_private = is_private
                    )
        
        #Se não for none, vai criar os generos_favoritos do usuário na tabela genero_usuario
        if generos_favoritos is not None:
            for genero in generos_id:
                usuario.generos_favoritos.add(genero)
            

        
        usuario.save()
        return Response({'status': 201, 'msg': 'registered successfully'})
        


class UsuarioModelViewSet(ModelViewSet):
    # authenticacao
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

    # Listar usuarios
    def list(self, request):
        usuario = Usuario.objects.all()
        serial = UsuarioSerializer(usuario, many=True)
        if len(serial.data) > 0:
            return Response({
                'status': 302, 'Usuario': serial.data
            })
        return Response({'status': 204, 'msg': 'No Content'})

    # retornar os dados do usuário
    @action(methods=["get"], detail=False)
    def me(self, request):
        usuario = Usuario.objects.get(Vinculado=request.user)
        serial = UsuarioSerializer(usuario)
        return Response({'status': 302, 'Usuario': serial.data})

    def patch(self, request):
        obj = Usuario.objects.get(Vinculado=request.user)
        name = request.data.get('first name')
        email = request.data.get('email')
        tel = request.data.get('telefone')
        cpf = request.data.get('cpf')
        obj.Vinculado.first_name = name
        obj.Vinculado.email = email
        obj.Telefone = tel
        obj.cpf = cpf
        obj.Vinculado.save()
        obj.save()
        return Response({'status': 200, 'msg': 'OK'})

    def delete(self, request):
        obj = Usuario.objects.get(id=request.user)
        obj.Vinculado.delete()
        obj.delete()
        return Response({'status': 200, 'msg': 'Deleted'})