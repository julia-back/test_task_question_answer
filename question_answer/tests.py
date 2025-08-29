from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Question, Answer
from users.models import User


class QuestionAPITestCase(APITestCase):

    def setUp(self):
        self.question = Question.objects.create(text="Hi!")
        self.just_user = User.objects.create_user(username="no_staff", email="no@staff.com", password="123", is_staff=False)
        self.user_staff = User.objects.create_user(username="staff", email="staff@staff.com", password="123", is_staff=True)

        self.user_owner = User.objects.create_user(username="no_staff_2", email="no@staff_2.com", password="123",
                                                   is_staff=False)
        self.answer = Answer.objects.create(question_id=self.question, user_id=self.user_owner, text="hi")

    def test_question_list(self):
        url = reverse("question_answer:question_list")

        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual("Hi!", response.json()[0].get("text"))
        self.assertTrue(response.json()[0].get("created_at"))
        self.assertTrue(response.json()[0].get("id"))

    def test_question_retrieve(self):
        url = reverse("question_answer:question_retrieve", args=[self.question.id])

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
        url = reverse("question_answer:question_delete", args=[self.question.id])
        response = self.client.delete(url)
        self.assertEqual(401, response.status_code)

        self.client.force_authenticate(self.just_user)
        response = self.client.delete(url)
        self.assertEqual(403, response.status_code)

        self.client.force_authenticate(self.user_staff)
        response = self.client.delete(url)
        self.assertEqual(204, response.status_code)

        url_answer_retrieve = reverse("question_answer:answer_retrieve", args=[self.answer.id])
        response = self.client.get(url_answer_retrieve)
        self.assertEqual(404, response.status_code)
        self.assertEqual("No Answer matches the given query.", response.json().get("detail"))


class AnswerAPITestCase(APITestCase):

    def setUp(self):
        self.user_owner = User.objects.create_user(username="no_staff", email="no@staff.com", password="123", is_staff=False)
        self.user_other = User.objects.create_user(username="no_staff_2", email="no@staff_2.com", password="123", is_staff=False)
        self.question = Question.objects.create(text="Hi!")
        self.answer = Answer.objects.create(question_id=self.question, user_id=self.user_owner, text="hi")

    def test_answer_retrieve(self):
        url = reverse("question_answer:answer_retrieve", args=[self.answer.id])
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

        self.client.force_authenticate(self.user_owner)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(self.answer.id, response.json().get("id"))
        self.assertEqual(self.answer.question_id.id, response.json().get("question_id"))
        self.assertEqual(self.answer.user_id.id, response.json().get("user_id"))
        self.assertEqual(self.answer.text, response.json().get("text"))

    def test_answer_create(self):
        url = reverse("question_answer:answer_create")
        response = self.client.post(url)
        self.assertEqual(401, response.status_code)

        self.client.force_authenticate(self.user_owner)
        response = self.client.post(url, data={"question_id": self.question.id, "text": "hi"})
        self.assertEqual(201, response.status_code)
        self.assertTrue(response.json().get("question_id"))
        self.assertTrue(response.json().get("text"))

        response = self.client.post(url, data={"question_id": (self.question.id + 1), "text": "hi"})
        self.assertEqual(400, response.status_code)
        self.assertTrue(response.json().get("question_id")[0].startswith("Invalid pk"))

    def test_answer_delete(self):
        url = reverse("question_answer:answer_delete", args=[self.answer.id])
        response = self.client.delete(url)
        self.assertEqual(401, response.status_code)

        self.client.force_authenticate(self.user_other)
        response = self.client.delete(url)
        self.assertEqual(403, response.status_code)

        self.client.force_authenticate(self.user_owner)
        response = self.client.delete(url)
        self.assertEqual(204, response.status_code)
