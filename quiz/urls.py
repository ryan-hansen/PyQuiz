from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),
]