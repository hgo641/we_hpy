from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import *

# return redirect('~~', ~~) 로 리다이렉트 해주는것과 직접 render을 리턴해주는것의
# 차이를 알아봐야할 것 같습니다.

def signUp(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            auth.login(request, user)
            return render(request, "login.html")
        else:
            return render(request, "signUp.html")
    else:
        form = UserForm()
        return render(request, "signUp.html")
    #     if request.POST['password'] == request.POST['confirm']:
    #         username = request.POST["username"]
    #         email = request.POST["email"]
    #         password = request.POST["password"]
    #         gender = request.POST["gender"]
    #         birth_date = request.POST["birth_date"]

    #         user = User.objects.create_user(username, email, gender, birth_date, password)
 
    #         user.save()
    #         auth.login(request,user)

    #     return render(request, "login.html")
    # return render(request, "sign_up.html")

def login(request):
    if request.method == 'POST':
        #form = LoginForm(request.POST)
        #email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)#이메일 왜 안되지 ? 왜 안되지? 왜안되지 ??? 일단 유저네임으로
        if user is not None:
            auth.login(request, user)
            #print(email)
            print('loginsuccess')
            return redirect('/')
        else:
            #print(email)
            print(password)
            print('nooooo')
            return render(request, 'login.html',{'error':'username or password is incorrect'})
    else:
        return render(request, 'login.html')

# 로그아웃 뷰

def logout(request):
    auth.logout(request)
    return redirect('/')
        
    