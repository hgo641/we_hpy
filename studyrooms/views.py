from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from users.models import *
from django.contrib import auth
from django.core.paginator import Paginator

def studyroom(request, room_id):
    if request.user.is_authenticated:
        
        studyroom = Studyroom.objects.get(studyroom_number = room_id)
        # print(studyroom,type(studyroom))
        # print(request.user.mypage.study_room.all())
        # print(request.user.mypage.make_study.all())
        # print(request.user.study_rooms.all(),type(request.user.study_rooms.all()))
        # print(request.user.study_rooms.all()[0],type(request.user.study_rooms.all()[0]))
        
        # mypage = MyPage.objects.create(userId = request.user)
        # mypage.save()

        # if studyroom in request.user.study_rooms.all():
        if True:
            # 스터디룸에 등록되있을시에
            context = {
                'room_id' : room_id
            }
            return render(request, 'studyroom.html', context)
        else:
            # 스터디룸 가입 안되있을떄, 등록 request보내는 화면
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
