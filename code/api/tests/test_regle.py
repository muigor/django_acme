'''from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from api.models import Enseignant


# python manage.py test api/tests/test_regle.py --verbosity=2
#   python manage.py test api/tests --verbosity=2

class ApiTestCase(TestCase):
    fixtures = ['enseignants', 'ues', "regles", "exercices"]

    regle_url = 'http://localhost:8002/api/regles/'
    regle_new = {"id": 3, "nom": "regle3","description": "balise test", "exercices": [1]}
    regle_edited = regle_new.copy()
    regle_edited['nom'] += "edited"
        
    def setUp(self):
        self.anonymous = APIClient()
        self.connected = APIClient()
        self.connected.force_login(Enseignant.objects.get_or_create(username='testuser')[0])



    def test_anonymous_can_get_all_regle(self):
        response = self.anonymous.get(self.regle_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()[0]['id'], 1)
        self.assertEqual(response.json()[0]['nom'], "regle1")
        self.assertEqual(response.json()[1]['id'], 2)
        self.assertEqual(response.json()[1]['nom'], "regle2")
    
    def test_anonymous_can_get_one_regle(self):
        response = self.anonymous.get(self.regle_url + '1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_anonymous_can_not_add_regle(self):
        response = self.anonymous.post(self.regle_url, self.regle_new)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        

    def test_anonymous_can_not_update_regle(self):
        response = self.anonymous.put(self.regle_url + '1/', self.regle_edited)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_anonymous_can_not_delete_regle(self):
        response = self.anonymous.delete(self.regle_url + '1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_connected_can_get_all_regle(self):
        response = self.connected.get(self.regle_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()[0]['id'], 1)
        self.assertEqual(response.json()[0]['nom'], "regle1")
        self.assertEqual(response.json()[1]['id'], 2)
        self.assertEqual(response.json()[1]['nom'], "regle2")

    def test_connected_can_get_one_regle(self):
        
        response = self.connected.get(self.regle_url + '1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_connected_can_add_regle(self):
        response = self.connected.post(self.regle_url, self.regle_new)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.connected.get(self.regle_url + str(response.json()['id']) + '/')
        self.assertEqual(response.json()['id'], self.regle_new['id'])

    def test_connected_can_update_regle(self):
        response = self.connected.put(self.regle_url + '1/', self.regle_edited)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.connected.get(self.regle_url + '1/')
        self.assertEqual(response.json()['nom'], self.regle_edited['nom'])
        
    
    def test_connected_can_delete_regle(self):
        response = self.connected.delete(self.regle_url + '1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.connected.get(self.regle_url + '1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)'''