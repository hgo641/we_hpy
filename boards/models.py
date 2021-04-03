from django.db import models
from studyrooms.models import *
from users.models import *
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    thema = models.CharField(max_length=200) #자유게시판/ 질문게시판/ 정보게시판 이런거...
    author = models.OneToOneField(
        "users.User", on_delete=models.CASCADE)
    studyroom = models.ForeignKey('studyrooms.Studyroom', on_delete=models.CASCADE)

class Comment(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    board = models.ForeignKey('Post', on_delete=models.CASCADE)