from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Coustomer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12)
    image = models.ImageField(upload_to='accounts/images/')

    def __str__(self):
        return self.user.username
    