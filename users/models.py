from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Класс кастомной моделя пользователя."""

    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.email
