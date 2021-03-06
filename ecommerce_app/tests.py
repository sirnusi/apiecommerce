from rest_framework import status, test
from rest_framework_simplejwt import tokens
from django.urls import reverse
from . import models
from django.contrib.auth.models import User


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
        
    def test_category_ind(self):
        response = self.client.put(reverse('category-detail', args=(self.category.id, )))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_category_delete(self):
        response = self.client.delete(reverse('category-detail', args=(self.category.id, )))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        

class ProductTestCase(test.APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='sirnusi', password='Newpassword123')
        self.category = models.Category.objects.create(name='Food')
        self.product = models.Product.objects.create(name='Yam', category=self.category, 
                                                     description='Beautiful and heavy', owner=self.user,
                                                     price=200, image='./media/images/G.jpg/', quantity=7, active=False)
        self.refresh = tokens.RefreshToken.for_user(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.refresh.access_token}')
        
    def test_product_list(self):
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    # def test_product_create(self):
    #     data = {
    #         'name': 'Ketchup',
    #         'category': self.category.id,
    #         'description': 'Very sweet', 
    #         'owner': self.user.id,
    #         'image': './media/images/GWAGON.jpg/',
    #         'price': 500,
    #         'quantity': 5,
    #         'active': True,
    #     }
    #     response = self.client.post(reverse('product-create'), data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    # def test_product_update(self):
    #     response = self.client.put(reverse('product-detail', args=(self.product.id, )))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)