from rest_framework import routers
from .viewsets import * 

router = routers.DefaultRouter()

router.register(r'ues', UEViewSet)
router.register(r'enseignants', EnseignantViewSet)
router.register(r'exercices', ExerciceViewSet)
router.register(r'regles', RegleViewSet)




