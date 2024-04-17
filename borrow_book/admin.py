from django.contrib import admin
from .models import Borrowing
# Register your models here.
@admin.register(Borrowing)
class BorrowingAdmin(admin.ModelAdmin):
    list_display = ['book_name','username']

    def book_name(self, obj):
        return obj.book.title
    
    def username(self, obj):
        return obj.coustomer.user.username
