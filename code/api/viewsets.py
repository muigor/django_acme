from .models import *
from rest_framework import viewsets
from .serializers import *

class UEViewSet(viewsets.ModelViewSet):
    queryset = UE.objects.all()
    serializer_class = UESerializer

class RegleViewSet(viewsets.ModelViewSet):
    queryset = Regle.objects.all()
    serializer_class = RegleSerializer

class EnseignantViewSet(viewsets.ModelViewSet):
    queryset = Enseignant.objects.all()
    serializer_class = EnseignantSerializer
    
class ExerciceViewSet(viewsets.ModelViewSet):
    queryset = Exercice.objects.all()
    serializer_class = ExerciceSerializer
