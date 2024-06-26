from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import authenticate,login, logout
from .models import Coustomer
from django.contrib.auth.models import User
from .serializer import CustomerSerializer, RegistrationSerializer,LoginSerializer, UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status 
# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Coustomer.objects.all()
    serializer_class = CustomerSerializer
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RegistretionViewSet(APIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link = f"https://thebookishnook.onrender.com/accounts/active/{uid}/{token}"
            email_subject = "Confirm Your Email"
            email_body = render_to_string('confirm_email.html',{'confirm_link': confirm_link})
            email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()
            return Response("Check Your Email to Verify Account")
        return Response(serializer.errors)

def activate(request,uid64,token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except (User.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        return redirect('https://precious-llama-5a48dd.netlify.app/login')
    else:
        return redirect('https://precious-llama-5a48dd.netlify.app/registration')

class LoginViewSet(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username= username, password=password)
            if user:
                 token,_ = Token.objects.get_or_create(user=user)
                 login(request,user )
                 return Response({'token': token.key, 'userd_id': user.id})
            else:
                return Response({'error': 'Invalid Creadential'})
        
        return Response(serializer.errors)



def logout_view(request):
    logout(request)
    return redirect('login')