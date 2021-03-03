from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import auth


def studyroomMake(request):
    return render(request, 'make.html')


def join(request):
    return render(request, 'join.html')


def myRoom(request):
    return render(request, 'studyroom.html')
