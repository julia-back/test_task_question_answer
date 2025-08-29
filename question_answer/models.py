from django.db import models


class Question(models.Model):
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
