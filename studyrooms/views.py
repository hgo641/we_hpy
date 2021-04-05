from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from users.models import *
from applications.models import *
from django.contrib import auth
from django.core.paginator import Paginator
from .forms import StudyroomForm
from applications.models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
import json
import datetime
import calendar


def studyroom(request, room_id):
    if request.user.is_authenticated:
        # 스터디룸에 소속되어 있는지 확인하고 안되어 있으면 request페이지로 연결
        studyroom = get_object_or_404(Studyroom, pk=room_id)

        # 스터디룸 페이지
        if(studyroom in request.user.study_room.all()):
            taskCount = studyroom.progress_task_set.count()
            averageProgressRate = 0 if taskCount == 0 else sum(
                [progressRate.totalProgress for progressRate in studyroom.progress_rate_set.all()]) / taskCount
            context = {
                'room_id': room_id,
                'memberCount': studyroom.users.count(),
                'studyroomName': studyroom.studyroom_name,
                'totalStudyTime': sum([progressRate.totalHour for progressRate in studyroom.progress_rate_set.all()]),
                'averageProgressRate': averageProgressRate,

            }
            return render(request, 'studyrooms/studyroom.html', context)
        # 신청서 페이지
        else:
            context = {
                'studyName': studyroom.studyroom_name,
                'studyCaptain': studyroom.leader.username,
                'studyField': studyroom.studyroom_classification,
                'studyParticipants': studyroom.users.count(),
                'studyOpen': '공개범위가 이곳에 들어갑니다'
            }
            if(request.method == "POST"):
                studyroom = get_object_or_404(Studyroom, pk=room_id)
                if studyroom.application.filter(userId=request.user).count() == 0:
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
    if request.user.is_authenticated:
        context = {
            'room_id': room_id,
        }
        user = request.user
        studyroom = Studyroom.objects.get(pk=room_id)

        if user in studyroom.users.all():
            today = datetime.date.today()
            todayMonth = today.month
            todayYear = today.year

            # get PARAM에서 연/월 가져오기
            try:
                date = request.GET["date"]
                year, month = map(int, date.split('-'))
            except:
                year, month = todayYear, todayMonth

            startWeekday, lastDay = calendar.monthrange(year, month)

            lastMonth = str(year if month != 1 else year - 1) + \
                '-' + str(month - 1 if month != 1 else 12)
            nextMonth = str(year if month != 12 else year + 1) + \
                '-' + str(month + 1 if month != 12 else 1)

            weeks = [
                [{}, {}, {}, {}, {}, {}, {}],
                [{}, {}, {}, {}, {}, {}, {}],
                [{}, {}, {}, {}, {}, {}, {}],
                [{}, {}, {}, {}, {}, {}, {}],
                [{}, {}, {}, {}, {}, {}, {}],
                [{}, {}, {}, {}, {}, {}, {}],
            ]

            j = startWeekday + 1
            for i in range(lastDay):
                weeks[j//7][j % 7]['day'] = i + 1
                j += 1
            weeks[0][6]['tasks'] = ['hahaha', 'dodododo']

            # calendar.monthrange(2017, 3) => 2요일, 31 가장높은 일자

            # date.weekday로 요일 얻기 월 0 일 6
            #
            context = {
                'room_id': room_id,
                'weeks': weeks,
                'year': year,
                'month': month,
                'lastMonth': lastMonth,
                'nextMonth': nextMonth,

            }
            return render(request, 'studyrooms/studyroomCalendar.html', context)
        else:
            return redirect('studyroom', room_id)
    else:
        return redirect('login')



def studyroomBoard(request, room_id):
    context = {
        'room_id': room_id,
    }
    if request.user.is_authenticated:
        user = request.user
        studyroom = Studyroom.objects.get(pk=room_id)
        if user in studyroom.users.all():
            return render(request, 'studyrooms/studyroomBoard.html', context)
        else:
            return redirect('studyroom', room_id)
    else:
        return redirect('login')

def studyroomMember(request, room_id):
    context = {
        'room_id': room_id,
    }
    if request.user.is_authenticated:
        user = request.user
        studyroom = Studyroom.objects.get(pk=room_id)
        if user in studyroom.users.all():
            context['users'] = studyroom.users.all()
            return render(request, 'studyrooms/studyroomMember.html', context)
        else:
            return redirect('studyroom', room_id)
    else:
        return redirect('login')

def studyroomTime(request, room_id):
    context = {
        'room_id': room_id,
    }
    if request.user.is_authenticated:
        user = request.user
        studyroom = Studyroom.objects.get(pk=room_id)

        if user in studyroom.users.all():
            context['study_time'] = studyroom.progress_rate_set.all().get(user=user).totalHour
            return render(request, 'studyrooms/studyroomTime.html', context)
        else:
            return redirect('studyroom', room_id)
    else:
        return redirect('login')


def studyroomProgress(request, room_id):
    context = {
        'room_id': room_id,
    }
    if request.user.is_authenticated:
        user = request.user
        studyroom = Studyroom.objects.get(pk=room_id)
        if user in studyroom.users.all():
            context['tasks'] = studyroom.progress_task_set.all()
            return render(request, 'studyrooms/studyroomProgress.html', context)
        else:
            return redirect('studyroom', room_id)
    else:
        return redirect('login')

def studyroomConfirm(request, room_id):
    if request.user.is_authenticated:
        studyroom = Studyroom.objects.get(pk=room_id)
        if studyroom.leader == request.user:
            if(request.method == "POST"):
                data = json.loads(request.body.decode())
                application = Application.objects.get(pk=int(data['appId']))
                if data['choice'] == 'accept':
                    application.userId.study_room.add(studyroom)
                    application.delete()

                elif data['choice'] == 'decline':
                    # 추후에 신청 거절/수락 여부를 알림등으로 알리는 기능 추가
                    application.delete()

                return HttpResponse("잘못된 접근")
            else:
                applications = studyroom.application.all()
                context = {
                    'room_id': room_id,
                    'isCaptain': True,
                    'applications': applications,
                }
                return render(request, 'studyrooms/studyroomConfirm.html', context)
        else:
            context = {
                'room_id': room_id,
                'isCaptain': False,
            }
            return render(request, 'studyrooms/studyroomConfirm.html', context)
    else:
        return redirect('login')

# 이후에 스터디장 이전 기능 추가


def studyroomManage(request, room_id):
    if request.user.is_authenticated:
        studyroom = Studyroom.objects.get(pk=room_id)
        if studyroom.leader == request.user:
            if(request.method == "POST"):
                data = json.loads(request.body.decode())
                user = User.objects.get(pk=int(data['userId']))
                if data['choice'] == 'ban':
                    if user == studyroom.leader:
                        # js로 처리해서 작동안함. 이후에 ajax로 경고할 수 있는지 확인
                        context = {
                            'room_id': room_id,
                            'isCaptain': True,
                            'users': studyroom.users.all(),
                            'error_message': '스터디장은 추방할 수 없습니다',
                        }
                        return render(request, 'studyrooms/studyroomManage.html', context)
                    else:
                        user.study_room.remove(studyroom)

                        return HttpResponse("잘못된 접근")
            else:
                context = {
                    'room_id': room_id,
                    'isCaptain': True,
                    'users': studyroom.users.all(),
                }
                return render(request, 'studyrooms/studyroomManage.html', context)
        else:
            context = {
                'room_id': room_id,
                'isCaptain': False,
            }
            return render(request, 'studyrooms/studyroomManage.html', context)
    else:
        return redirect('login')


def studyroomGoal(request, room_id):
    studyroom = Studyroom.objects.get(pk=room_id)
    if request.user.is_authenticated:
        if studyroom.leader == request.user:
            context = {
                'room_id': room_id,
                'isCaptain': True,
                'tasks': studyroom.progress_task_set.all()
            }
            if request.method == 'POST':
                goalContent = request.POST.get('textarea-goal')
                if len(goalContent) == 0:
                    context.update({'error_message': '내용은 공백일 수 없습니다'})
                    return render(request, 'studyrooms/studyroomGoal.html', context)

                studyroom.progress_task_set.create(task=goalContent)
                return render(request, 'studyrooms/studyroomGoal.html', context)
            else:
                return render(request, 'studyrooms/studyroomGoal.html', context)
        else:
            context = {
                'room_id': room_id,
                'isCaptain': False
            }
            return render(request, 'studyrooms/studyroomGoal.html', context)
    else:
        return redirect('login')


def studyroomMake(request):
    # value들중 blank가 있으면 안되게 수정
    if request.user.is_authenticated:
        if request.method == "POST":
            form = StudyroomForm(request.POST)
            if form.is_valid():
                studyroom = Studyroom()
                studyroom.studyroom_name = form.cleaned_data["studyroom_name"]
                studyroom.studyroom_classification = form.cleaned_data["studyroom_classification"]
                studyroom.leader = request.user
                studyroom.save()
                studyroom.users.add(request.user)
                return redirect('studyroom', studyroom.pk)
            else:
                error = form.errors
                context = ({'error_message': error})
                return render(request, 'studyrooms/make.html', context)

            # roomPage = "/studyroom/room/" + str(post.studyroom_number)

        else:

            return render(request, 'studyrooms/make.html')
    else:
        return redirect('login')


def studyroomMy(request):
    if request.user.is_authenticated:
        STUDYROOMSPERPAGE = 24  # 페이지당 들어갈 스터디룸 숫자
        studyrooms = request.user.study_room.all()

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
