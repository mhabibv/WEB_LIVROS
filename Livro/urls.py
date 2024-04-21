from django.urls import path
from .views import LivroModelViewSet, LivroViewSet
from rest_framework.routers import DefaultRouter

Lrouter = DefaultRouter()
Lrouter.register(r'livro/create', LivroModelViewSet, basename = 'livro_create')

urlpatterns = [
    path('livros', LivroViewSet.as_view({'get': 'list_livros'}), name='listar_livros'),
    path('livros/<int:pk>/', LivroViewSet.as_view({'get': 'list_detaield'}), name='listar_detalhes_livros'),
    path('autores/<int:autor_id>/livros', LivroViewSet.as_view({'get': 'list_livro_autor'}), name='listar_livros_autor'),


]

