from django import forms
from django.forms.widgets import RadioSelect
from django.contrib import admin

# Register your models here.

from .models import *


class QuestionAdminForm(forms.ModelForm):
    CHOICES = (
        (True, 'Yes'),
        (False, 'No'),
    )
    answer = forms.TypedChoiceField(choices=CHOICES, widget=RadioSelect, label='Answer')


class QuestionInline(admin.TabularInline):
    model = Question
    exclude = ('created', 'modified')
    form = QuestionAdminForm


class QuizAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'instruction')
        }),
        ('Timestamps', {
            'classes': ('collapse',),
            'fields': ('created', 'modified')
        })
    )
    inlines = (QuestionInline,)


admin.site.register(Quiz, QuizAdmin)