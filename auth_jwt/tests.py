from rest_framework.test import APITestCase
from django.urls import reverse
from users.models import User


class TokenAPITestCase(APITestCase):

    def setUp(self):
        self.test_user = User.objects.create_user(username="testuser", email="test@email.com", password="testpsw1234", is_active=True)

    def test_token_obtain_pair(self):
        # проверяем необходимость юзернейма и пароля для получения токенов
        url = reverse("auth_jwt:token")
        response = self.client.post(url)
        self.assertEqual(400, response.status_code)
        self.assertEqual(["This field is required."], response.json().get("username"))
        self.assertEqual(["This field is required."], response.json().get("password"))

        # проверяем корректное получение токенов
        url = reverse("auth_jwt:token")
        response = self.client.post(url, data={"username": self.test_user.username, "password": "testpsw1234"})
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.json().get("access"))
        self.assertTrue(response.json().get("refresh"))
        self.refresh = response.json().get("refresh")

    def test_token_refresh(self):
        # получаем первоначальную пару токенов
        url = reverse("auth_jwt:token")
        response = self.client.post(url, data={"username": self.test_user.username, "password": "testpsw1234"})
        refresh_token = response.json().get("refresh")

        # проверяем необходимоcть refresh токена
        url = reverse("auth_jwt:token_refresh")
        response = self.client.post(url)
        self.assertEqual(400, response.status_code)
        self.assertEqual(["This field is required."], response.json().get("refresh"))

        # проверяем корректное получение access токена
        url = reverse("auth_jwt:token_refresh")
        response = self.client.post(url, data={"refresh": refresh_token})
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.json().get("access"))
        self.assertFalse(response.json().get("refresh"))
