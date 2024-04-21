from .views import UsuarioModelViewSet, RegisterView
from django.urls import path

urlpatterns = [
   path('register/', RegisterView.as_view()),


]