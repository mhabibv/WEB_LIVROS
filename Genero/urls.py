from django.urls import path
from .views import GeneroModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'generos', GeneroModelViewSet, basename='generos')

urlpatterns = router.urls