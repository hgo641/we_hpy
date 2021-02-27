


from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    # path('/studyroom', views.login, name='studyroom'),
    # path('/studyroom/found', views.login, name='studyroom'),
    path('make/', views.studyroomMake, name='studyroomMake'),

    path('my/', views.studyroomMy, name='studyroomMy'),

    # path('/studyroom/room/<roomNum>', views.login, name='studyroom'),
    # path('/studyroom/room/<roomNum>/private', views.login, name= 'studyroom'),
    # path('/studyroom/room/<roomNum>/public', views.login, name='studyroom'),

]

    