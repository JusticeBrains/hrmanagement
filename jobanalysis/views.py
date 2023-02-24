from django.shortcuts import render
from rest_framework import viewsets

from . import models as jobanalysis_model
from . import serializers


class JobAnalysisViewSet(viewsets.ModelViewSet):
    queryset = jobanalysis_model.JobAnalysis.objects.all()
    serializer_class = serializers.JobAnalysisSerializer


class JobAnalysisDutiesViewSet(viewsets.ModelViewSet):
    queryset = jobanalysis_model.JobAnalysisDuties.objects.all()
    serializer_class = serializers.JobAnalysisDutiesSerializer


class JobRequirementsViewSet(viewsets.ModelViewSet):
    queryset = jobanalysis_model.JobAnalysisRequirement.objects.all()
    serializer_class = serializers.JobAnalysisRequirementSerializer


class JobAnalysisSupervisionViewSet(viewsets.ModelViewSet):
    queryset = jobanalysis_model.JobAnalysisSupervision.objects.all()
    serializer_class = serializers.JobAnalysisSupervisionSerializer


class JobAnalysisContactViewSet(viewsets.ModelViewSet):
    queryset = jobanalysis_model.JobAnalysisContact.objects.all()
    serializer_class = serializers.JobAnalysisContactSerializer


class JobAnalysisAuthorityLimitViewSet(viewsets.ModelViewSet):
    queryset = jobanalysis_model.JobAnalysisAuthorityLimit.objects.all()
    serializer_class = serializers.JobAnalysisAuthorityuLimitSerializer


class JobAnalysisDemandViewSet(viewsets.ModelViewSet):
    queryset = jobanalysis_model.JobAnalysisDemand.objects.all()
    serializer_class = serializers.JobAnalysisDemandSerializer


class JobAnalysisRequirementViewSet(viewsets.ModelViewSet):
    queryset = jobanalysis_model.JobAnalysisRequirement.objects.all()
    serializer_class = serializers.JobAnalysisRequirementSerializer


class JobEvaluationViewSet(viewsets.ModelViewSet):
    queryset = jobanalysis_model.JobEvaluation.objects.all()
    serializer_class = serializers.JobEvaluationSerializer
