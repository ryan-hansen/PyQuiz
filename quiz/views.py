import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from quiz.models import Quiz, Question, UserAnswer


def index(request):
    return redirect('list')


@login_required()
def quiz_list(request):
    """
    Get all available quizzes.
    """
    q_list = list()
    quizzes = Quiz.objects.all()
    for q in quizzes:
        correct = q.get_results(request.user)
        total = float(q.questions.all().count())
        results = int(round(float(len(correct)) / total * 100))
        q_dict = {
            'id': q.id,
            'title': q.title,
            'created': q.created,
            'percent_complete': int(q.percent_complete(request.user)),
            'results': results,
        }
        q_list.append(q_dict)
    return render(request, 'quiz/quiz_list.html', context=dict(quizzes=q_list))


@login_required()
def take_quiz(request, quiz_id):
    """
    Load the selected quiz.
    """
    quiz = Quiz.objects.get(id=quiz_id)

    context = dict(quiz=quiz, question=quiz.get_next_question(request.user))

    return render(request, 'quiz/quiz.html', context=context)


def next_question(request, quiz_id):
    """
    Get the next unanswered question for the selected quiz.
    """
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
    """
    POST: Set the user's answer for the current question.
    """
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