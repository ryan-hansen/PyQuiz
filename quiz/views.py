import json

from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from quiz.models import Quiz


def index(request):
    return redirect('list')


@login_required()
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/quiz_list.html', context=dict(quizzes=quizzes))


@login_required()
def take_quiz(request, quiz_id):
    q = Quiz.objects.get(id=quiz_id)

    context = dict(q=q, next_question=q.get_next_question(request.user))

    return render(request, 'quiz/quiz.html', context=context)


def next_question(request, quiz_id):
    q = Quiz.objects.get(id=quiz_id).get_next_question(request.user)
    question = dict(question=q.question)

    response = json.dumps(question)
    return HttpResponse(response)



def logout_view(request):
    logout(request)

    return redirect('list')