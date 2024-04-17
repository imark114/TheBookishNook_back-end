from django.shortcuts import render
from rest_framework import viewsets
from .models import Borrowing
from .serializers import BorrowingSerializers
# Create your views here.

class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializers

    def get_queryset(self):
        queryset = super().get_queryset()
        customer_id = self.request.query_params.get('customer_id')
        if customer_id:
            queryset = queryset.filter(coustomer_id=customer_id)
        return queryset
    