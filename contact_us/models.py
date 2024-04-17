from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=15)
    phone = models.CharField(max_length=12)
    text_body = models.TextField()
    class Meta:
        verbose_name_plural = 'Conact Us'
    def __str__(self):
        return self.name
    