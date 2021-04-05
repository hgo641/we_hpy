from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    path('board/<str:board_id>/<int:studyroom_id>', views.board, name='board'),
    path('new/<int:room_id>/<str:board_thema>', views.postnew, name='postnew'),
    path('study/<str:board_thema>/<int:room_id>', views.postcreate, name='postcreate'),
    path('detail/<int:post_id>',views.detail,name="detail"),
    path('postdelete/<int:post_id>',views.postdelete,name="postdelete"),
]
