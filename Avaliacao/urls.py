from django.urls import path
from .views import AvaliacaoCreateAPIView, ComentarioCreateAPIView, AvaliacaoListAPIView,ComentariosListAPIView

urlpatterns = [
    path('avaliacoes/create/', AvaliacaoCreateAPIView.as_view(), name='avaliacao-create'),
    path('avaliacoes/delete/<int:avaliacao_id>/', AvaliacaoCreateAPIView.as_view(), name='avaliacao-delete'),
    path('comentarios/create/', ComentarioCreateAPIView.as_view(), name='comentario-create'),
    path('comentarios/delete/<int:comentario_id>/', ComentarioCreateAPIView.as_view(), name='comentario-delete'),
    path('avaliacoes/<int:livro_id>/',AvaliacaoListAPIView.as_view(),name = 'avaliacoes-list'),
    path('comentarios/<int:avaliacao_id>/',ComentariosListAPIView.as_view(),name = 'comentarios-list'),
]