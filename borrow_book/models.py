from django.db import models
from django.contrib.auth.models import User
from book.models import Book
# Create your models here.
class Borrowing(models.Model):
   coustomer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
   book = models.ForeignKey(Book, on_delete=models.CASCADE)
   borrow_date = models.DateTimeField(auto_now_add=True)
   return_date = models.DateField(blank=True, null=True)
   def __str__(self):
       return self.book.title

