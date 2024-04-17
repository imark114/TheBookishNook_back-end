from django.contrib import admin
from .models import Category, Book, Review, Wishlist
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',),}

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['coustomer', 'book']

    def coustomer(self, obj):
        return obj.reviwer.username
    def book(self,obj):
        obj.book.title

admin.site.register(Wishlist)