from core.test.testcase import CustomTestCase
from polls.models import Question, Choice


class ExampleTestCase(CustomTestCase):
    def setUp(self):
        self.question = Question.objects.create(question_text='Your question?')

    def test_question_created(self):
        question = Question.objects.get(pk=self.question.pk)
        self.assertEqual('Your question?', question.question_text)

    def test_choice_created(self):
        question = Question.objects.get(pk=self.question.pk)
        choice = Choice.objects.create(question=question, choice_text='this choice?')
