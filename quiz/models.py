from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

QUIZ_TYPES = (
    (1, 'Fact'),
    (2, 'Opinion'),
)

class Quiz(models.Model):
    title = models.CharField(max_length=250)
    instruction = models.TextField()
    quiz_type = models.IntegerField(choices=QUIZ_TYPES, default=1)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, null=True)
    question = models.CharField(max_length=250, null=True)
    answer = models.BooleanField()
    feedback = models.TextField(null=True)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)


class UserAnswer(models.Model):
    user = models.ForeignKey(User, null=True)
    question = models.ForeignKey(Question, null=True)
    answer = models.BooleanField()
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)