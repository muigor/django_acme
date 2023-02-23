'''from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from api.models import Enseignant


# python manage.py test api/tests/test_ue.py --verbosity=2
#   python manage.py test api/tests --verbosity=2

class ApiTestCase(TestCase):
    fixtures = ['enseignants', 'ues']

    ue_url = 'http://localhost:8002/api/ues/'
    ue_new = {"id": 3, "codeUE" :'MIC001', "nom": "math","enseignants": [1]}
    ue_edited = ue_new.copy()
    ue_edited['nom'] += "edited"
        
    def setUp(self):
        self.anonymous = APIClient()
        self.connected = APIClient()
        #self.connected.force_login(Enseignant.objects.get_or_create(username='testuser')[0])
        self.connected.force_authenticate(Enseignant.objects.get_or_create(username='testuser')[0])

    def test_anonymous_can_get_all_ue(self):
        response = self.anonymous.get(self.ue_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()[0]['id'], 1)
        self.assertEqual(response.json()[0]['nom'], "ue1")
        self.assertEqual(response.json()[1]['id'], 2)
        self.assertEqual(response.json()[1]['nom'], "ue2")
    
    def test_anonymous_can_get_one_ue(self):
        response = self.anonymous.get(self.ue_url + '1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_anonymous_can_not_add_ue(self):
        response = self.anonymous.post(self.ue_url, self.ue_new)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        

    def test_anonymous_can_not_update_ue(self):
        response = self.anonymous.put(self.ue_url + '1/', self.ue_edited)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_anonymous_can_not_delete_ue(self):
        response = self.anonymous.delete(self.ue_url + '1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_connected_can_get_all_ue(self):
        response = self.connected.get(self.ue_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()[0]['id'], 1)
        self.assertEqual(response.json()[0]['nom'], "ue1")
        self.assertEqual(response.json()[1]['id'], 2)
        self.assertEqual(response.json()[1]['nom'], "ue2")

    def test_connected_can_get_one_ue(self):
        
        response = self.connected.get(self.ue_url + '1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_connected_can_add_ue(self):
        response = self.connected.post(self.ue_url, self.ue_new)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.connected.get(self.ue_url + str(response.json()['id']) + '/')
        self.assertEqual(response.json()['id'], self.ue_new['id'])

    def test_connected_can_update_ue(self):
        response = self.connected.put(self.ue_url + '1/', self.ue_edited)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.connected.get(self.ue_url + '1/')
        self.assertEqual(response.json()['nom'], self.ue_edited['nom'])
        
    
    def test_connected_can_delete_ue(self):
        response = self.connected.delete(self.ue_url + '1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.connected.get(self.ue_url + '1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)'''