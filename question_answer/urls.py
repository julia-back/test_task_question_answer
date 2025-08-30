from django.urls import path

from . import views
from .apps import QuestionAnswerConfig

app_name = QuestionAnswerConfig.name


urlpatterns = [
    path("questions/", views.QuestionListAPIView.as_view(), name="question_list"),
    path("question/<int:pk>/", views.QuestionRetrieveAPIView.as_view(), name="question_retrieve"),
    path("question/new/", views.QuestionCreateAPIView.as_view(), name="question_create"),
    path("question/<int:pk>/delete", views.QuestionDestroyAPIView.as_view(), name="question_delete"),
    path("answer/<int:pk>/", views.AnswerRetrieveAPIView.as_view(), name="answer_retrieve"),
    path("answer/new/", views.AnswerCreateAPIView.as_view(), name="answer_create"),
    path("answer/<int:pk>/delete/", views.AnswerDestroyAPIView.as_view(), name="answer_delete"),
]
