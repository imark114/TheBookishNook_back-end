from django.shortcuts import render
from rest_framework import viewsets
from .models import ContactUs
from .serializers import ContuctUsSerializer
# Create your views here.

class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContuctUsSerializer