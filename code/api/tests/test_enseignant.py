from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User



class ApiTestCase(TestCase):
    fixtures = ['enseignants', 'users', 'ues']

    enseignant_url = 'http://localhost:8002/api/enseignants/'
    enseignant_new = {"id": 3, "nom": "Isnard", "prenom": "Stéphane", "adresse_mail": "test@test.com", "mot_de_passe": "mdp","ues": [1]}
    enseignant_edited = enseignant_new.copy()
    enseignant_edited['nom'] += "edited"
    
    
    def setUp(self):
        self.anonymous = APIClient()
        self.connected = APIClient()
        root = User.objects.get(username='root')
        connected = APIClient()
        connected.force_authenticate(user=root) 



    def test_connected_can_get_all_enseignant(self):
        response = self.connected.get(self.enseignant_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()[0]['id'], 1)
        self.assertEqual(response.json()[0]['nom'], "El")
        self.assertEqual(response.json()[1]['id'], 2)
        self.assertEqual(response.json()[1]['nom'], "lola")
    
    def test_connected_can_get_one_enseignant(self):
        
        response = self.connected.get(self.enseignant_url + '1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)



    # python manage.py test api/tests --verbosity=2
    def test_connected_can_add_enseignant(self):
        response = self.connected.post(self.enseignant_url, self.enseignant_new)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.connected.get(self.enseignant_url + str(response.json()['id']) + '/')
        self.assertEqual(response.json()['id'], self.enseignant_new['id'])
        
    
    def test_connected_can_update_enseignant(self):
        response = self.connected.put(self.enseignant_url + '1/', self.enseignant_edited)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.connected.get(self.enseignant_url + '1/')
        self.assertEqual(response.json()['nom'], self.enseignant_edited['nom'])
        
    
    def test_connected_can_delete_enseignant(self):
        response = self.connected.delete(self.enseignant_url + '1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.connected.get(self.enseignant_url + '1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)