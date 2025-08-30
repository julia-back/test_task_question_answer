import logging

from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import Answer, Question
from .permissions import IsOwner
from .serializers import (AnswerSerializer, CreateAnswerSerializer, CreateQuestionSerializer, QuestionSerializer,
                          RetrieveQuestionSerializer)

view_logger = logging.getLogger("view")


class AnswerRetrieveAPIView(generics.RetrieveAPIView):
    """Класс представления деталей ответа."""

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerCreateAPIView(generics.CreateAPIView):
    """
    Класс представления для создания ответа. Переопределяет
    метод сохранения ответа, проставляя значения поля user_id.
    """

    queryset = Answer.objects.all()
    serializer_class = CreateAnswerSerializer

    def perform_create(self, serializer):
        """Метод сохранения ответа. Проставляет значения поля, определяющего автора ответа."""

        serializer.save(user_id=self.request.user)
        view_logger.debug(f"Сохранен ответ на вопрос с пользователем {self.request.user.email}")


class AnswerDestroyAPIView(generics.DestroyAPIView):
    """Класс представления для удаления ответа."""

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class QuestionListAPIView(generics.ListAPIView):
    """Класс представления для получения списка вопросов."""

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionRetrieveAPIView(generics.RetrieveAPIView):
    """Класс представления для получения деталей конкретного вопроса."""

    queryset = Question.objects.all()
    serializer_class = RetrieveQuestionSerializer


class QuestionCreateAPIView(generics.CreateAPIView):
    """Класс представления для создания вопроса."""

    queryset = Question.objects.all()
    serializer_class = CreateQuestionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class QuestionDestroyAPIView(generics.DestroyAPIView):
    """Класс представления для удаления вопроса."""

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
