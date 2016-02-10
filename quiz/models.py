from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Quiz(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)


class Question(models.Model):
    quiz = Quiz
    question = models.CharField(max_length=250)
    answer = models.BooleanField()
    feedback = models.TextField(null=True)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)


class UserAnswer(models.Model):
    question = Question
    answer = models.BooleanField()
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)