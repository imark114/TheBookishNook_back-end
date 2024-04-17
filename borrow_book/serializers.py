from rest_framework import serializers
from .models import Borrowing

class BorrowingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = '__all__'