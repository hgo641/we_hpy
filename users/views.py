from django.shortcuts import render, redirect, get_object_or_404
from .models import *


def sign_up(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        gender = request.POST["gender"]
        birth_date = request.POST["birth_date"]

        user = User.objects.create_user(
            username, email, gender, birth_date, password)
        #user.username = username
        #user.password = password
        # user.gender = gender
        # user.birth_date = birth_date
        user.save()

        return render(request, "login_test.html")
    return render(request, "sign_up.html")
# Create your views here.
