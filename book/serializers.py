from rest_framework import serializers
from .models import Book, Category,Review,Wishlist

class BookSerilizer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)
    class Meta:
        model = Book
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'