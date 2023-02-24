from rest_framework import serializers

from . import models as interview_models


class InterviewScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = interview_models.InterviewScore
        fields = "__all__"


class InterviewTestQuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = interview_models.InterviewTestQuestionnaire
        fields = "__all__"


class InterviewPanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = interview_models.InterviewPanel
        fields = "__all__"


class MedicalQuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = interview_models.MedicalQuestionnaire
        fields = "__all__"


class ApplicationMedicalTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = interview_models.ApplicantMedicalTest
        fields = "__all__"
