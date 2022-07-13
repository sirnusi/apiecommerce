from rest_framework import status, test
from django.urls import reverse
from . import models
from django.contrib.auth.models import User
# Create your tests here.

class CategoryTestCase(test.APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='sirnusi', password='Newpassword123')
        self.category = models.Category.objects.create(name='Food')    
    
    def test_category_list(self):
        response = self.client.get(reverse('category-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_category_create(self):
        data = {
            'name':'Phone'
        }
        response = self.client.post(reverse('category-create'), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)