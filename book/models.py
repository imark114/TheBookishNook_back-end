from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=25)
    slug = models.SlugField(max_length=25)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to="book/images/")
    author = models.CharField(max_length=15)
    isbn = models.CharField(max_length=13)
    description = models.TextField(blank=True, null=True)
    quantiry = models.PositiveIntegerField(blank=True, null=True)
    publication_date = models.DateField()
    genres = models.ManyToManyField(Category)
    is_avilable = models.BooleanField(default=True)
    can_review = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]

class Review(models.Model):
    reviwer = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    rating = models.CharField(choices=STAR_CHOICES, max_length=10)

    def __str__(self):
        return f"Coustomer:{self.reviwer.username} Book: {self.book.title}"

class Wishlist(models.Model):
    coustomer = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return f"buyer: {self.coustomer.username}:"
    
