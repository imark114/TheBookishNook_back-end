from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('list', views.BookViewSet)
router.register('categories', views.CategoryViewSet)
router.register('review', views.ReviewViewSet)
router.register('wishlist', views.WishlistViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
