import json

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from .models import *
from .serializers import *

# Create your tests here.

"""class MaterielTestCase(APITestCase):
    def test_materiel_creation(self):
        data = {"nom": "test nom"}
        response = self.client.post("/gestion-salle/materiel/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_materiel_list(self):
        response = self.client.get("/gestion-salle/materiel/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
"""
        
