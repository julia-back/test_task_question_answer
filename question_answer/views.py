from rest_framework import generics
from .models import Question, Answer
from .serializers import QuestionSerializer, CreateQuestionSerializer, RetrieveQuestionSerializer, AnswerSerializer, CreateAnswerSerializer


class AnswerRetrieveAPIView(generics.RetrieveAPIView):

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = []


class AnswerCreateAPIView(generics.CreateAPIView):

    queryset = Answer.objects.all()
    serializer_class = CreateAnswerSerializer
    permission_classes = []


class AnswerDestroyAPIView(generics.DestroyAPIView):

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = []


class QuestionListAPIView(generics.ListAPIView):

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = []


class QuestionRetrieveAPIView(generics.RetrieveAPIView):

    queryset = Question.objects.all()
    serializer_class = RetrieveQuestionSerializer
    permission_classes = []


class QuestionCreateAPIView(generics.CreateAPIView):

    queryset = Question.objects.all()
    serializer_class = CreateQuestionSerializer
    permission_classes = []


class QuestionDestroyAPIView(generics.DestroyAPIView):

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = []
