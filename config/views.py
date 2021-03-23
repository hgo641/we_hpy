from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.template import loader

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
        gender = "other"
        if request.user.gender == 'f':
            gender = "female"
        elif request.user.gender == 'm':
            gender = "male"
        context = {
            'name' :request.user.username,
            'email' : request.user.email,
            'gender' : gender,
            'birthDate' : request.user.birth_date,
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