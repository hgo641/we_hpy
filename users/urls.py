from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    path('signUp/', views.signUp, name="signUp"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),

]
