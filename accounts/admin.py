from django.contrib import admin
from .models import Coustomer
# Register your models here.

@admin.register(Coustomer)
class CoustomerAdmin(admin.ModelAdmin):
    list_display = ['username', 'phone_number']

    def username(self, obj):
        return obj.user.username
