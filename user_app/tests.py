from rest_framework import status, test
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework_simplejwt import tokens

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
        
        
class LoginLogoutTestCase(test.APITestCase):
    
    def setUp(self):
        self.user = User.objects.create(username='sirnusi',
                                        password='Newpassword123'
                                        )
        
        self.refresh = tokens.RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.refresh.access_token))
       

    def test_login(self):
        data = {
            'username': 'sirnusi', 
            'password': 'Newpassword123',
        }
             
        response = self.client.post(reverse('token_obtain_pair'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        