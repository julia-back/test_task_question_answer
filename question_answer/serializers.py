from rest_framework import serializers

from .models import Answer, Question


class AnswerSerializer(serializers.ModelSerializer):
    """Класс сериализатора ответа."""

    class Meta:
        model = Answer
        fields = "__all__"


class CreateAnswerSerializer(serializers.ModelSerializer):
    """Класс сериализатора создания ответа."""

    class Meta:
        model = Answer
        fields = ["question_id", "text"]


class QuestionSerializer(serializers.ModelSerializer):
    """Класс сериализатора вопроса."""

    class Meta:
        model = Question
        fields = "__all__"


class RetrieveQuestionSerializer(serializers.ModelSerializer):
    """Класс сериализатора для получения деталей конктерного вопроса."""

    answer_set = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = "__all__"


class CreateQuestionSerializer(serializers.ModelSerializer):
    """Класс сериализатора создания вопроса."""

    class Meta:
        model = Question
        fields = ["text"]
