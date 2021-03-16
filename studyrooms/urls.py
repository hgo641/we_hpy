

from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    path('make/', views.studyroomMake, name='studyroomMake'),
    path('my/', views.studyroomMy, name='studyroomMy'),
    path('join/', views.studyroomJoin, name='studyroomJoin'),    
    path('room/<int:room_id>', views.studyroom, name='studyroom'),
    
]
