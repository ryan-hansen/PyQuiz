from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.quiz_list, name='list'),
    url(r'^(?P<quiz_id>[0-9]+)/next/$', views.next_question, name='next_question'),
    url(r'^take/(?P<quiz_id>[0-9]+)/$', views.take_quiz, name='quiz'),
]