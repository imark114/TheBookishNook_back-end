from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('customer', views.CustomerViewSet)
router.register('list', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.RegistretionViewSet.as_view(), name='register'),
    path('active/<uid64>/<token>/', views.activate, name='activate'),
    path('login/', views.LoginViewSet.as_view(), name='login'),
    path('logout/', views.LogoutApiView.as_view(),name='logout'),
]
