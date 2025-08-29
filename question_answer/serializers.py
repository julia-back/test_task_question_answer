from rest_framework import serializers

from .models import Answer, Question


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = "__all__"


class CreateAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ["question_id", "text"]


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = "__all__"


class RetrieveQuestionSerializer(serializers.ModelSerializer):

    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = "__all__"


class CreateQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ["text"]
