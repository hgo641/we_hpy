from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import auth


def studyroomJoin(request):
    return render(request, 'join.html')


def studyroomMake(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            post = Studyroom()
            post.studyroom_name = request.POST["studyroom_name"]
            post.studyroom_classification = request.POST["studyroom_classification"]
            post.leader_Id = request.user
            post.save()
            return redirect('studyroomMy')
        else:
            context = {
                'tags': [
                    {'name': 'A'},
                    {'name': 'B'},
                    {'name': 'C'},
                ]
            }
            return render(request, 'make.html', context)
    else:
        return redirect('login')


def studyroomMy(request):
    if request.user.is_authenticated:

        studyrooms = request.user.study_rooms.all()
        return render(request, 'my.html', {'studyrooms': studyrooms})
    else:
        return redirect('login')

def studyroomJoin(request):
    if request.user.is_authenticated:
        context = {
            'studyrooms' : [
                {
                    'number' : '1',
                    'name' : 'name1',
                    'field' : 'field1',
                    'abc' : 'abcd'
                },
                {
                    'number' : '2',
                    'name' : 'name2',
                    'field' : 'field2',
                    'abc' : 'abcd'
                }
            ]
        }
        return render(request, 'join.html', context)
    else:
        return redirect('login')
