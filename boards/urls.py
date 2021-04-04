from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    path('board/<str:board_id>/<int:studyroom_id>', views.board, name='board'),
    
]
