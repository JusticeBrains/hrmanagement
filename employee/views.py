from django.shortcuts import render

from rest_framework import viewsets
from . import models as employee_model
from . import serializers


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = employee_model.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer


class AppraisalAreaViewSet(viewsets.ModelViewSet):
    queryset = employee_model.AppraisalAreas.objects.all()
    serializer_class = serializers.AppraisalAreaSerializer


class EmployeeAppraisalViewSet(viewsets.ModelViewSet):
    queryset = employee_model.EmployeeAppraisal.objects.all()
    serializer_class = serializers.EmployeeAppraisalSerializer


class EmployeeAppraisalResponseViewSet(viewsets.ModelViewSet):
    queryset = employee_model.EmployeeAppraisalResponse.objects.all()
    serializer_class = serializers.EmployeeAppraisalResponseSerializer


class EmployeePromotionViewSet(viewsets.ModelViewSet):
    queryset = employee_model.EmployeePromotion.objects.all()
    serializer_class = serializers.EmployeePromotionSerializer


class EmployeeMedicalViewSet(viewsets.ModelViewSet):
    queryset = employee_model.EmployeeMedicals.objects.all()
    serializer_class = serializers.EmployeeMedicalSerializer


class EmployeeDisciplinaryActionViewSet(viewsets.ModelViewSet):
    queryset = employee_model.EmployeeDisciplinaryActions.objects.all()
    serializer_class = serializers.EmployeeDisciplinaryActionsSerializer


class EmployeePolicyViewSet(viewsets.ModelViewSet):
    queryset = employee_model.EmployeePolicy.objects.all()
    serializer_class = serializers.EmployeePolicySerializer


class EmployeePayReviewViewSet(viewsets.ModelViewSet):
    queryset = employee_model.EmployeePayReview.objects.all()
    serializer_class = serializers.EmployeePayReviewSerializer
