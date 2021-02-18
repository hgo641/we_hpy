from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    path('', views.sign_up, name="sign_up"),
    path('login/', views.login, name="login"),

]
