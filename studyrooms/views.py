from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from users.models import *
from django.contrib import auth
from django.core.paginator import Paginator
from .forms import StudyroomForm
from applications.models import *


def studyroom(request, room_id):
    if request.user.is_authenticated:
        # 스터디룸에 소속되어 있는지 확인하고 안되어 있으면 request페이지로 연결
        studyroom = get_object_or_404(Studyroom, pk = room_id)

        if(studyroom in request.user.mypage.study_room.all()):
            context = {
                'room_id': room_id
            }
            return render(request, 'studyrooms/studyroom.html', context)
        else:
            context = {
                'studyName': studyroom.studyroom_name,
                'studyCaptain': studyroom.leader_Id.username,
                'studyField': studyroom.studyroom_classification,
                'studyParticipants': len(studyroom.mypages.all()),
                'studyOpen': '공개범위가 이곳에 들어갑니다'
            }
            if(request.method == "POST"):
                studyroom = get_object_or_404(Studyroom, pk = room_id)
                if len(studyroom.application.filter(userId = request.user)) == 0:
                    application = Application()
                    application.userId = request.user 
                    application.studyroomId = studyroom
                    application.text = request.POST["studyroom_classification"]
                    application.save()
                else:
                    context['error'] = '이미 스터디룸 참여 요청을 보냈습니다'
                    return render(request, 'studyrooms/request.html', context)
                return redirect('main')
            else:
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

def studyroomConfirm(request, room_id):
    context = {
        'room_id': room_id,
        'isCaptain' : True if Studyroom.objects.get(pk = room_id).leader_Id == request.user else False,
        
    }
    return render(request, 'studyrooms/studyroomConfirm.html', context)

def studyroomManage(request, room_id):
    context = {
        'room_id': room_id,
        'isCaptain' : True if Studyroom.objects.get(pk = room_id).leader_Id == request.user else False,
        
    }
    return render(request, 'studyrooms/studyroomManage.html', context)

#def studyroomApply(request, room_id):
#    if (request.user.is_authenticated):
#        if (request.method == "POST"):
#            studyroom = get_object_or_404(Studyroom, pk = room_id)
#            application = Application()
#            application.userId = request.user 
#            application.studyroomId = studyroom


#    else:
#        return redirect('login')

# def studyroomManagement(request, room_id):


def studyroomMake(request):
    # value들중 blank가 있으면 안되게 수정
    if request.user.is_authenticated:
        if request.method == "POST":
            form = StudyroomForm(request.POST)
            if form.is_valid():
                studyroom = Studyroom()
                studyroom.studyroom_name = form.cleaned_data["studyroom_name"]
                studyroom.studyroom_classification = form.cleaned_data["studyroom_classification"]
                studyroom.leader_Id = request.user
                studyroom.save()
                studyroom.mypages.set([request.user.id])

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


