from django.shortcuts import render
from django.http import HttpResponse
# render와 HttpResponse의 차이?

# def login(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)

def login(request):
    return HttpResponse("Test Login")
