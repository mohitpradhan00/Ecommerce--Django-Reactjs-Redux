from ecomapp import views
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)

urlpatterns = [
    path('', views.getRoutes, name = "getRoutes"),
    path('products/', views.getProducts, name = "getProducts"),
    path('product/<str:pk>', views.getProduct, name = "getProduct"),
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/profile/',views.getUserProfile, name = "getUserProfile"),
    path('users/',views.getUsers, name = "getUsers"),
    path('users/register',views.registerUser, name="register"),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate'),
]
