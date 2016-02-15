"""
This test suite was created to be run with pytest; however, there are some Django dependencies that make it unlikely
that these tests will run successfully as-is outside of the develop environment I run them in.  In other words, I can
run them from inside PyCharm (my IDE), which has built-in facility for running pytest tests and which sets up the
necessary Django environment, but I can't currently run them with py.test from the command line.
"""

import django
import random

django.setup()

from django.contrib.auth.models import User
from quiz.models import Quiz, Question, UserAnswer


class TestQuiz:

    def setup_method(self, test_method):
        username = 'testuser'
        quiz_title = u'PyTest Quiz'

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

        self.user = u
        self.quiz = q
        self.quiz_title = quiz_title
        self.username = username

        self._create_questions()

    def teardown_method(self, test_method):
        self.user.delete()
        self.quiz.delete()

    def test_has_results(self):
        """
        Test whether or not a quiz has been started, i.e. any of the questions have been answered.
        """
        self._answer_questions()
        results = self.quiz.get_results(self.user)
        assert len(results) > 0

    def test_next_question(self):
        """
        Test that the next unanswered question of a given quiz is returned successfully.
        TODO: Currently only tests that a question object is returned. Should ideally test that it is indeed the next
        question in the quiz.
        """
        q = self.quiz.get_next_question(self.user)
        assert isinstance(q, Question)

        self._answer_questions()
        q = self.quiz.get_next_question(self.user)
        assert q is None

    def test_percent_complete(self):
        """
        Test proper determination of a completed quiz (no more unanswered questions)
        """
        num_answer = random.randint(1, 5)
        self._answer_questions(num_answer)

        assert self.quiz.percent_complete(self.user) == float(num_answer) / float(5) * 100

    def _create_questions(self, qnum=5):
        """
        Create <qnum> questions for a quiz.
        :param qnum: (int) The number of questions to create
        :return: None
        """

        for q in xrange(1, qnum + 1):
            question = 'Question {0}'.format(q)
            feedback = 'Feedback {0}'.format(q)
            answer = q % 2 == 0
            Question(quiz=self.quiz, question=question, answer=answer, feedback=feedback).save()

    def _answer_questions(self, qnum=None):
        """
        Helper function to answer <qnum> questions of a quiz.
        :param qnum: (int) The number of questions to answer.  None = answer all questions.
        """
        all_questions = self.quiz.questions.all()

        if qnum:
            all_questions = all_questions[:qnum]

        for q in all_questions:
            UserAnswer(user=self.user, question=q, answer=True).save()
