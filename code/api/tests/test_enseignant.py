from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from api.models import Enseignant



class ApiTestCase(TestCase):
    fixtures = ['enseignants', 'ues']

    enseignant_url = 'http://localhost:8000/api/enseignants/'
    enseignant_new = {"username": "Isnard", "email": "test@test.com", "password": "mdp","ues": [1], "first_name":"Isnard","last_name": "Stéphane"}
    enseignant_edited = enseignant_new.copy()
    enseignant_edited['username'] += "edited"

    # python manage.py test api/tests --verbosity=2
    
    def setUp(self):
        self.anonymous = APIClient()
        self.connected = APIClient()
        #self.connected.force_login(Enseignant.objects.get_or_create(username='testuser')[0]) 
        self.connected.force_authenticate(Enseignant.objects.get_or_create(username='testuser')[0])
        
        

       

        
    def test_anonymous_can_get_all_enseignant(self):
        response = self.anonymous.get(self.enseignant_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_anonymous_can_get_one_enseignant(self):
        response = self.anonymous.get(self.enseignant_url + '1/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_anonymous_can_add_enseignant(self):
        response = self.anonymous.post(self.enseignant_url, self.enseignant_new)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        

    def test_anonymous_can_update_enseignant(self):
        response = self.anonymous.put(self.enseignant_url + '1/', self.enseignant_edited)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_anonymous_can_delete_enseignant(self):
        response = self.anonymous.delete(self.enseignant_url + '1/')
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)




    def test_connected_can_get_all_enseignant(self):
        response = self.connected.get(self.enseignant_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()[0]['username'], "El")
        self.assertEqual(response.json()[1]['username'], "lola")
    
    def test_connected_can_get_one_enseignant(self):
        
        response = self.connected.get(self.enseignant_url + '1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)



    # python manage.py test api/tests --verbosity=2
    def test_connected_can_add_enseignant(self):
        response = self.connected.post(self.enseignant_url, self.enseignant_new)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.connected.get(self.enseignant_url + str(response.json()['id']) + '/')
        self.assertEqual(response.json()['username'], self.enseignant_new['username'])
        
    
    def test_connected_can_update_enseignant(self):
        response = self.connected.put(self.enseignant_url + '1/', self.enseignant_edited)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.connected.get(self.enseignant_url + '1/')
        self.assertEqual(response.json()['username'], self.enseignant_edited['username'])
        
    
    def test_connected_can_delete_enseignant(self):
        response = self.connected.delete(self.enseignant_url + '1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.connected.get(self.enseignant_url + '1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
