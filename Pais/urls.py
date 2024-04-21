from Pais.views import PaisModelViewSet
from rest_framework.routers import DefaultRouter

Prouter = DefaultRouter()
Prouter.register(r'Pais', PaisModelViewSet, basename = 'Paises')