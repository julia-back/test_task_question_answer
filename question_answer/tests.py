from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Question, Answer
from users.models import User


class QuestionAPITestCase(APITestCase):

    def setUp(self):
        self.just_user = User.objects.create_user(username="no_staff", email="no@staff.com", password="123", is_staff=False)
        self.user_staff = User.objects.create_user(username="staff", email="staff@staff.com", password="123", is_staff=True)

    def test_question_list(self):
        question = Question.objects.create(id=1, text="Hi!")

        url = reverse("question_answer:question_list")

        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual("Hi!", response.json()[0].get("text"))
        self.assertTrue(response.json()[0].get("created_at"))
        self.assertTrue(response.json()[0].get("id"))

    def test_question_retrieve(self):
        question = Question.objects.create(id=2, text="Hi!")

        url = reverse("question_answer:question_retrieve", args=[question.id])

        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual("Hi!", response.json().get("text"))
        self.assertTrue(response.json().get("created_at"))
        self.assertTrue(response.json().get("id"))

    def test_question_create(self):
        url = reverse("question_answer:question_create")

        response = self.client.post(url, data={})
        self.assertEqual(401, response.status_code)

        self.client.force_authenticate(self.just_user)
        response = self.client.post(url, data={})
        self.assertEqual(403, response.status_code)

        self.client.force_authenticate(self.user_staff)
        response = self.client.post(url, data={"text": "hi"})
        self.assertEqual(201, response.status_code)
        self.assertEqual("hi", response.json().get("text"))

    def test_question_destroy(self):
        question = Question.objects.create(id=3, text="Hi!")

        url = reverse("question_answer:question_delete", args=[3])
        response = self.client.delete(url)
        self.assertEqual(401, response.status_code)

        self.client.force_authenticate(self.just_user)
        response = self.client.delete(url)
        self.assertEqual(403, response.status_code)

        self.client.force_authenticate(self.user_staff)
        response = self.client.delete(url)
        self.assertEqual(204, response.status_code)


class AnswerAPITestCase(APITestCase):

    def setUp(self):
        pass

    def test_(self):
        pass
