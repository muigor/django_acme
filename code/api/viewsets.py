from .models import *
from rest_framework import viewsets
from .serializers import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly 

class UEViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset = UE.objects.all()
    serializer_class = UESerializer

class RegleViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset = Regle.objects.all()
    serializer_class = RegleSerializer

class EnseignantViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes=[IsAuthenticated]
    queryset = Enseignant.objects.all()
    serializer_class = EnseignantSerializer
    
class ExerciceViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset = Exercice.objects.all()
    serializer_class = ExerciceSerializer
