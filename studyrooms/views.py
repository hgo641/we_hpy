from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import auth

        
def studyroomMake(request):
    if request.user.is_authenticated:
        context = {
            'tags' : [
                {'name' : 'A'},
                {'name' : 'B'},
                {'name' : 'C'},
            ]
        }
        return render(request, 'make.html', context)
    else:
        return redirect('login')

def studyroomMy(request):
    if request.user.is_authenticated:
        context = {
            'studyrooms' : [
                {'subject': 'subjectTest', 'content' : 'contentText'},
                {'subject': '제목 테스트2', 'content' : '내용 테스트2'},
            ]
        }
        return render(request, 'my.html', context)
    else:
        return redirect('login')
