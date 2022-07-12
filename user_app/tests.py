from rest_framework import status, test
from django.contrib.auth.models import User
from django.urls import reverse


# Create your tests here.
class RegistrationTestCase(test.APITestCase):
    
    def test_register(self):
        data = {
            'username': 'sirnusi',
            'email': 'nusi@gmail.com',
            'password': 'Newpassword123',
            'password2': 'Newpassword123'  
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)