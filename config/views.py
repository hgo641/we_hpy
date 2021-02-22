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

def found(request):
    template = loader.get_template('login/found.html')
    context = {
        'testData' : "testData is testData"
    }
    return HttpResponse(template.render(context, request))

def idfound(request):
    template = loader.get_template('login/idfound.html')
    context = {
        'testData' : "testData is testData"
    }
    return HttpResponse(template.render(context, request))

def pwfound(request):
    template = loader.get_template('login/pwfound.html')
    context = {
        'testData' : "testData is testData"
    }
    return HttpResponse(template.render(context, request))

def mypage(request):
    template = loader.get_template('mypage/mypage.html')
    context = {
        'testData' : "testData is testData"
    }
    return HttpResponse(template.render(context, request))