from django.db import models
from users.models import User


class Question(models.Model):

    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):

    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.SET(0))
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
