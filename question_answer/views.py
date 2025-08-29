import logging

from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import Answer, Question
from .permissions import IsOwner
from .serializers import (AnswerSerializer, CreateAnswerSerializer, CreateQuestionSerializer, QuestionSerializer,
                          RetrieveQuestionSerializer)

view_logger = logging.getLogger("view")


class AnswerRetrieveAPIView(generics.RetrieveAPIView):

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerCreateAPIView(generics.CreateAPIView):

    queryset = Answer.objects.all()
    serializer_class = CreateAnswerSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
        view_logger.debug(f"Сохранен ответ на вопрос с пользователем {self.request.user.email}")


class AnswerDestroyAPIView(generics.DestroyAPIView):

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class QuestionListAPIView(generics.ListAPIView):

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionRetrieveAPIView(generics.RetrieveAPIView):

    queryset = Question.objects.all()
    serializer_class = RetrieveQuestionSerializer


class QuestionCreateAPIView(generics.CreateAPIView):

    queryset = Question.objects.all()
    serializer_class = CreateQuestionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class QuestionDestroyAPIView(generics.DestroyAPIView):

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
