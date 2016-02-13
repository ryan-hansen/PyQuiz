import json

from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from quiz.models import Quiz, Question, UserAnswer


def index(request):
    return redirect('list')


@login_required()
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/quiz_list.html', context=dict(quizzes=quizzes))


@login_required()
def take_quiz(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)

    context = dict(quiz=quiz, question=quiz.get_next_question(request.user))

    return render(request, 'quiz/quiz.html', context=context)


def next_question(request, quiz_id):
    q = Quiz.objects.get(id=quiz_id)
    next_q = q.get_next_question(request.user)

    if next_q:
        result = {
            'finished': False,
            'question': next_q.question,
            'id': next_q.id,
        }
    else:
        result = {
            'finished': True,
            'correct': len(q.get_results(request.user)),
            'total': q.questions.all().count()
        }
    response = json.dumps(result)
    return HttpResponse(response)


@csrf_exempt  # temporarily exempt for development purposes
def user_answer(request):
    question = None
    try:
        question = Question.objects.get(id=request.POST.get('question_id'))
        raw_answer = request.POST.get('answer')

        if raw_answer == 'up':
            answer = True
        else:
            answer = False

        ua = UserAnswer(
            user=request.user,
            question=question,
            answer=answer
        )
        ua.save()

        result = ua.is_correct
    except Question.DoesNotExist:
        result = 'Failed - Invalid Question'

    response = dict(result=result, feedback=question.feedback)

    return HttpResponse(json.dumps(response))


def logout_view(request):
    logout(request)

    return redirect('list')