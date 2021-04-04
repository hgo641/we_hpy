from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import *
from users.models import *
from studyrooms.models import *

# Create your views here.
def board(request, board_id, studyroom_id):
    print(request)
    print(board_id)
    print("board2입니다")
    #boardid=get_object_or_404(Post,thema=board_id)
    studyroom = get_object_or_404(Studyroom, pk = studyroom_id)
    posts = Post.objects.filter(studyroom = studyroom)
    posts =posts.filter(thema=board_id)
    return render(request, 'boards/boardlist.html', {'posts' : posts})