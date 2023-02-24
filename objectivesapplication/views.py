from django.shortcuts import render

from rest_framework import viewsets

from . import models as obj_model
from . import serializers


class CorporateValueViewSet(viewsets.ModelViewSet):
    queryset = obj_model.CorporateValues.objects.all()
    serializer_class = serializers.CorporateValuesSerializer


class CooperateObjectiveViewSet(viewsets.ModelViewSet):
    queryset = obj_model.CooperateObjectives.objects.all()
    serializer_class = serializers.CooperateObjectivesSerializer


class DepartmentObjectiveViewSet(viewsets.ModelViewSet):
    queryset = obj_model.DepartmentalObjectives.objects.all()
    serializer_class = serializers.DepartmentObjectivesSerializer


class ObjectiveReviewLinesViewSet(viewsets.ModelViewSet):
    queryset = obj_model.ObjectiveReviewLines.objects.all()
    serializer_class = serializers.ObjectiveReviewLinesSerilizer


class IndividualObjectiveLineViewSet(viewsets.ModelViewSet):
    queryset = obj_model.IndividualObjectiveLines.objects.all()
    serializer_class = serializers.IndividualObjectiveLinesSerializer


class IndividualObjectiveSettingViewSet(viewsets.ModelViewSet):
    queryset = obj_model.IndividualObjectiveSetting.objects.all()
    serializer_class = serializers.IndividualObjectiveSettingSerializer


class IndividualObjectiveReviewViewSet(viewsets.ModelViewSet):
    queryset = obj_model.IndividualObjectiveReview.objects.all()
    serializer_class = serializers.IndividualObjectiveReviewSerializer
