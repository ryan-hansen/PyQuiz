import requests

from behave import *
from bs4 import BeautifulSoup


@given(u'I am a user')
def step_impl(context):
    assert True


@when(u'I visit the home page')
def step_impl(context):
    r = requests.get('http://127.0.0.1:8000')
    context.page = r.content
    assert r.status_code == 200


@then(u'The title says "Welcome to Django"')
def step_impl(context):
    soup = BeautifulSoup(context.page, 'html.parser')
    title = soup.find('title').text
    assert title == u'Welcome to Django'