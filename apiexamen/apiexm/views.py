from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework import viewsets

class UsuarioViewSet(viewsets.ModelViewSet):
 
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()