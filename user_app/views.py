from django.shortcuts import render
from .serializers import RegistrationSerializer
from rest_framework import decorators, response, status
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.
@decorators.api_view(['POST'])
def registration_view(request):
    
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            
            data['Response'] = 'Registration Successful'
            data['username'] = account.username
            data['email'] = account.email
            
            refresh = RefreshToken.for_user(account)
            data['tokens'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        else:
            data = serializer.errors
                
        return response.Response(data, status=status.HTTP_201_CREATED)