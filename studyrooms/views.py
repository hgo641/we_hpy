from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from users.models import *
from django.contrib import auth
from django.core.paginator import Paginator

def studyroom(request, room_id):
    if request.user.is_authenticated:
        # 스터디룸에 소속되어 있는지 확인하고 안되어 있으면 request페이지로 연결
        check = 0
        studyrooms = list(request.user.study_rooms.all())
        for studyroom in studyrooms:
            if(studyroom.studyroom_number == room_id):
               check = 1 
                
        if(check==1):
            context = {
                'room_id' : room_id
            }
            return render(request, 'studyroom.html', context)
        else:
            context = {
                'studyName' : 'test',
                'studyCaptain' : '땡컨',
                'studyField' : 'idk',
                'studyOpen' : 'notreallynicenamingsence'
            }
            return render(request, 'request.html', context)
    else:
        return redirect('login')


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
        STUDYROOMSPERPAGE = 5 # 페이지당 들어갈 스터디룸 숫자
        studyrooms = request.user.study_rooms.all()
        paginator = Paginator(studyrooms, STUDYROOMSPERPAGE)
        page = request.GET.get('page')
        modifiedStudyrooms = paginator.get_page(page)
        pages = range(1, paginator.num_pages + 1)

        context = {
            'studyrooms': modifiedStudyrooms,
            'pages': pages
        }
        return render(request, 'my.html', context)
    else:
        return redirect('login')

def studyroomJoin(request):
    if request.user.is_authenticated:
        context = {
            'studyrooms' : [
                {
                    'number' : 1,
                    'name' : 'name1',
                    'field' : 'field1',
                    'id' : 1
                },
                {
                    'number' : 2,
                    'name' : 'name2',
                    'field' : 'field2',
                    'id' : 2
                }
            ]
        }
        return render(request, 'join.html', context)
    else:
        return redirect('login')
