from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.template import loader

# from .forms import LoginForm

# def login(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)

# render() 함수는 request 객체를 첫번째 인수로 받고, 템플릿 이름을 두번째 인수로 받으며,
# context 사전형 객체를 세전째 선택적(optional) 인수로 받습니다. 
# 인수로 지정된 context로 표현된 템플릿의 HttpResponse 객체가 반환됩니다.

def main(request):
    return render(request, 'main/main.html')

def myPage(request):
    if request.user.is_authenticated:
        context = {
            'name' : request.user.username,
            'email' : request.user.email,
            "studyroom_number" : str(len(request.user.study_rooms.all())) + '개',
        }
        return render(request, 'mypage/mypage.html', context)
    else:
        return redirect('login')

def myInfo(request):
    if request.user.is_authenticated:
        context = {
            'test' : 'test'
        }
        return render(request, 'mypage/myinfo.html', context)
    else:
        return redirect('login')

def myCalender(request):
    if request.user.is_authenticated:
        context = {
            'test' : 'test'
        }
        return render(request, 'mypage/mycalender.html', context)
    else:
        return redirect('login')