from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('loginpage/', views.loginpage, name="loginpage"),
    
    path('signuppage/', views.signuppage, name="signuppage"),
    path('logoutPage/', views.logoutPage, name="logoutPage"),
    
]