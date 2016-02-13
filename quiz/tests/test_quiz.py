import django
import requests

django.setup()

from django.contrib.auth.models import User
from quiz.models import Quiz, Question, UserAnswer


class TestQuiz:

    def setup_method(self, test_method):
        username = 'testuser'
        quiz_title = u'PyTest Quiz'
        question_title = u'PyTest Quiz Question 1'

        try:
            u = User.objects.get(username=username)
        except User.DoesNotExist:
            u = User(username=username, first_name='Test', last_name='User')
            u.set_password('testuserpass')
            u.save()

        try:
            q = Quiz.objects.get(title=quiz_title)
        except Quiz.DoesNotExist:
            q = Quiz(title=quiz_title, instruction='PyTest creating a quiz', quiz_type=1)
            q.save()

        try:
            qu = Question.objects.get(question=question_title)
        except Question.DoesNotExist:
            qu = Question(quiz=q, question=question_title, answer=True, feedback='Well done')
            qu.save()

        self.user = u
        self.quiz = q
        self.question = qu
        self.question_title = question_title
        self.quiz_title = quiz_title
        self.username = username

    def teardown_method(self, test_method):
        self.user.delete()
        self.quiz.delete()

    def test_quiz_has_results(self):
        a = UserAnswer(user=self.user, question=self.question, answer=True)
        a.save()
        results = self.quiz.get_results(self.user)
        assert len(results) > 0

    def test_quiz_next_question(self):
        q = self.quiz.get_next_question(self.user)
        assert isinstance(q, Question)

        self._answer_all()
        q = self.quiz.get_next_question(self.user)
        assert q is None

    def test_quiz_is_complete(self):
        self._answer_all()
        assert self.quiz.get_next_question(self.user) is None

    def _answer_all(self):
        for q in self.quiz.questions.all():
            UserAnswer(user=self.user, question=q, answer=True).save()
