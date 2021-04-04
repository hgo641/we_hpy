from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from users.models import *
from studyrooms.models import *

# Create your views here.
def board(request, board_id, studyroom_id):
    studyroom = get_object_or_404(Studyroom, pk = studyroom_id)
    posts = Post.objects.filter(studyroom = studyroom)
    posts =posts.filter(thema=board_id)
    context = {
        'room_id' : studyroom_id,
        'posts' : posts,
        'board_thema' : board_id
    }
    return render(request, 'boards/boardlist.html', context)

	
def postnew(request,room_id, board_thema):
    context = {
        'room_id':room_id,
        'board_thema' : board_thema,
    }
    return render(request, 'boards/postnew.html', context)

    	
def postcreate(request, room_id,board_thema):
    print(request.method)
    if(request.method == 'POST'):
        post = Post()
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.thema = board_thema
        post.author = request.user
        studyroom = get_object_or_404(Studyroom, pk = room_id)
        post.studyroom = studyroom
        post.save()
        context = {
        'room_id':room_id,
        'board_thema' : board_thema,
    }
    return redirect('/boards/board/'+board_thema+'/'+str(room_id))
