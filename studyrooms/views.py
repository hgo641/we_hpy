from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import auth

        
def studyroomMake(request):
    if request.user.is_authenticated:
        return render(request, 'make.html')
    else:
        return redirect('/')
