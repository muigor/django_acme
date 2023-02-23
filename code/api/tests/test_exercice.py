from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from api.models import Enseignant

#   python manage.py test api/tests --verbosity=2

class ApiTestCase(TestCase):
    fixtures = ['enseignants', 'ues', "regles", "exercices"]

    exercice_url = 'http://localhost:8000/api/exercices/'
    exercice_new = {"id" :3,"nom": "exercice3", "ue": 1, "regles": [1]}
    exercice_edited = exercice_new.copy()
    exercice_edited['nom'] += "edited"

    def setUp(self):
        self.anonymous = APIClient()
        self.connected = APIClient()
        #self.connected.force_login(Enseignant.objects.get_or_create(username='testuser')[0])
        self.connected.force_authenticate(Enseignant.objects.get_or_create(username='testuser')[0])
    

    def test_anonymous_can_get_all_exercice(self):
        response = self.anonymous.get(self.exercice_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()[0]['id'], 1)
        self.assertEqual(response.json()[0]['nom'], "exercice1")
        self.assertEqual(response.json()[1]['id'], 2)
        self.assertEqual(response.json()[1]['nom'], "exercice2")
    
    def test_anonymous_can_get_one_exercice(self):
        response = self.anonymous.get(self.exercice_url + '1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_anonymous_can_not_add_exercice(self):
        response = self.anonymous.post(self.exercice_url, self.exercice_new)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        

    def test_anonymous_can_not_update_exercice(self):
        response = self.anonymous.put(self.exercice_url + '1/', self.exercice_edited)
        self.assertEqual(response.status_code,  status.HTTP_401_UNAUTHORIZED)
        
    def test_anonymous_can_not_delete_exercice(self):
        response = self.anonymous.delete(self.exercice_url + '1/')
        self.assertEqual(response.status_code,  status.HTTP_401_UNAUTHORIZED)


    def test_connected_can_get_all_exercice(self):
        response = self.connected.get(self.exercice_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()[0]['id'], 1)
        self.assertEqual(response.json()[0]['nom'], "exercice1")
        self.assertEqual(response.json()[1]['id'], 2)
        self.assertEqual(response.json()[1]['nom'], "exercice2")

    def test_connected_can_get_one_exercice(self):
        
        response = self.connected.get(self.exercice_url + '1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

#python manage.py test api/tests --verbosity=2
    def test_connected_can_add_exercice(self):
        response = self.connected.post(self.exercice_url, self.exercice_new )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.connected.get(self.exercice_url + str(response.json()['id']) + '/')
        self.assertEqual(response.json()['id'], self.exercice_new['id'])        

    def test_connected_can_update_exercice(self):
        response = self.connected.put(self.exercice_url + '1/', self.exercice_edited)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.connected.get(self.exercice_url + '1/')
        self.assertEqual(response.json()['nom'], self.exercice_edited['nom'])
        
    
    def test_connected_can_delete_exercice(self):
        response = self.connected.delete(self.exercice_url + '1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.connected.get(self.exercice_url + '1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        