from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from quiz.models import Quiz


def index(request):
    return render(request, 'index.html')


@login_required()
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/quiz_list.html', context=dict(quizzes=quizzes))


@login_required()
def take_quiz(request, quiz_id):
    q = Quiz.objects.get(id=quiz_id)

    context = dict(q=q)

    return render(request, 'quiz/quiz.html', context=context)


def logout_view(request):
    logout(request)

    return redirect('list')