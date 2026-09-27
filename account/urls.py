"""
URL configuration for workly project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from account import views

app_name="account"

urlpatterns = [
    path('',views.home,name='home'),
    path("gestcompny",views.gestcompny,name="gestcompny"),
    path('login', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('otp/', views.otp, name='otp'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('user_chat/', views.user_chat, name='user_chat'),
    
]
