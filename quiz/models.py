from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

QUIZ_TYPES = (
    (1, 'Fact'),
    (2, 'Opinion'),
)


class Quiz(models.Model):
    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'

    title = models.CharField(max_length=250)
    instruction = models.TextField()
    quiz_type = models.IntegerField(choices=QUIZ_TYPES, default=1)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def get_next_question(self, user):
        """
        Get the next unanswered question for this quiz
        :return: Question object
        """
        questions = Question.objects.filter(quiz=self)
        answered = Question.objects.filter(answers__user=user)
        return list(set(questions) - set(answered))[0]

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, null=True, related_name='questions')
    question = models.CharField(max_length=250, null=True)
    answer = models.BooleanField()
    feedback = models.TextField(null=True)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.question


class UserAnswer(models.Model):
    user = models.ForeignKey(User, null=True)
    question = models.ForeignKey(Question, null=True, related_name='answers')
    answer = models.BooleanField()
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    @property
    def is_correct(self):
        return self.answer == self.question.answer

    def __str__(self):
        return '{0}: {1}'.format(self.question, self.answer)