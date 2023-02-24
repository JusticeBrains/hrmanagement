from django.shortcuts import render
from rest_framework import viewsets

from . import serializers as interview_serializer
from . import models as interview_model


class InterviewScoreViewSet(viewsets.ModelViewSet):
    queryset = interview_model.InterviewScore.objects.all()
    serializer_class = interview_serializer.InterviewScoreSerializer


class InterviewTestQuestionnaireViewSet(viewsets.ModelViewSet):
    queryset = interview_model.InterviewTestQuestionnaire.objects.all()
    serializer_class = interview_serializer.InterviewScoreSerializer


class InterviewPanelViewSet(viewsets.ModelViewSet):
    queryset = interview_model.InterviewPanel.objects.all()
    serializer_class = interview_serializer.InterviewPanelSerializer


class MedicalQuestionnaireViewSet(viewsets.ModelViewSet):
    queryset = interview_model.MedicalQuestionnaire.objects.all()
    serializer_class = interview_serializer.MedicalQuestionnaireSerializer


class ApplicationMedicalTestViewSet(viewsets.ModelViewSet):
    queryset = interview_model.ApplicantMedicalTest.objects.all()
    serializer_class = interview_serializer.ApplicationMedicalTestSerializer
