from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from users.models import *
from django.contrib import auth
from django.core.paginator import Paginator


def studyroom(request, room_id):
    if request.user.is_authenticated:
        # 스터디룸에 소속되어 있는지 확인하고 안되어 있으면 request페이지로 연결

        # 모델 수정한 후에 조건변경
        # currentStudyroom = get_object_or_404(Studyroom, pk = room_id)
        # currentStudyroom in request.user.mypage.study_room.all()

        check = 0
        studyrooms = list(request.user.study_rooms.all())
        for studyroom in studyrooms:
            if(studyroom.studyroom_number == room_id):
                check = 1

        if(check == 1):
            context = {
                'room_id': room_id
            }
            return render(request, 'studyrooms/studyroom.html', context)
        else:
            context = {
                'studyName': 'test',
                'studyCaptain': '땡컨',
                'studyField': 'idk',
                'studyOpen': 'notreallynicenamingsence'
            }
            return render(request, 'studyrooms/request.html', context)
    else:
        return redirect('login')


def studyroomCalendar(request, room_id):
    context = {
        'room_id': room_id
    }
    return render(request, 'studyrooms/studyroomCalendar.html', context)


def studyroomBoard(request, room_id):
    context = {
        'room_id': room_id
    }
    return render(request, 'studyrooms/studyroomBoard.html', context)


def studyroomTime(request, room_id):
    context = {
        'room_id': room_id
    }
    return render(request, 'studyrooms/studyroomTime.html', context)


def studyroomProgress(request, room_id):
    context = {
        'room_id': room_id
    }
    return render(request, 'studyrooms/studyroomProgress.html', context)


def studyroomMake(request):
    # value들중 blank가 있으면 안되게 수정,
    # model form으로 하는게 좋을듯..?
    # 이것도 모델 수정후에 다시 수젇하기
    if request.user.is_authenticated:
        if request.method == "POST":
            post = Studyroom()
            post.studyroom_name = request.POST["studyroom_name"]
            post.studyroom_classification = request.POST["studyroom_classification"]
            post.leader_Id = request.user
            post.save()
            # roomPage = "/studyroom/room/" + str(post.studyroom_number)
            return redirect('studyroomMy')
        else:
            context = {
                'tags': [
                    {'name': 'A'},
                    {'name': 'B'},
                    {'name': 'C'},
                ]
            }
            return render(request, 'studyrooms/make.html', context)
    else:
        return redirect('login')


def studyroomMy(request):
    if request.user.is_authenticated:
        STUDYROOMSPERPAGE = 5  # 페이지당 들어갈 스터디룸 숫자
        studyrooms = request.user.study_rooms.all()

        paginator = Paginator(studyrooms, STUDYROOMSPERPAGE)
        page = request.GET.get('page')
        modifiedStudyrooms = paginator.get_page(page)
        pages = range(1, paginator.num_pages + 1)

        context = {
            'studyrooms': modifiedStudyrooms,
            'pages': pages
        }
        return render(request, 'studyrooms/my.html', context)
    else:
        return redirect('login')


def studyroomJoin(request):
    if request.user.is_authenticated:
        STUDYROOMSPERPAGE = 20  # 페이지당 숫자
        studyrooms = Studyroom.objects.all()

        paginator = Paginator(studyrooms, STUDYROOMSPERPAGE)
        page = request.GET.get('page')
        modifiedStudyrooms = paginator.get_page(page)
        pages = range(1, paginator.num_pages + 1)

        context = {
            'studyrooms': modifiedStudyrooms,
            'pages': pages
        }

        return render(request, 'studyrooms/join.html', context)
    else:
        return redirect('login')


def studyroomPublic(request, room_id):
    if request.user.is_authenticated:
        if True:
            return render(request, 'public.html')
        else:
            redirect('studyroom')
    else:
        return redirect('login')


def studyroomPrivate(request, room_id):
    if request.user.is_authenticated:
        if True:
            return render(request, 'private.html')
        else:
            redirect('studyroom')
    else:
        return redirect('login')
