from django.urls import path
from .views import AutorViewSet, AutorModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'autores/create', AutorModelViewSet, basename='autores')

urlpatterns = [
    path('autores/', AutorViewSet.as_view({'get': 'list_autor'}), name='autor-list'),
    path('autores/<int:pk>/', AutorViewSet.as_view({'get': 'autor_detaield'}), name='detalhe_autor'),

]

urlpatterns += router.urls