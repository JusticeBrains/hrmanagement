from django.shortcuts import render

from rest_framework import viewsets
from . import models as insuranceapp
from . import serializers


class InsurancePremiumPaymentViewSet(viewsets.ModelViewSet):
    queryset = insuranceapp.InsurancePremiumPayments.objects.all()
    serializer_class = serializers.InsurancePremiumPaymentsSerializer


class GroupLifeInsuranceViewSet(viewsets.ModelViewSet):
    queryset = insuranceapp.GroupLifeInsurance.objects.all()
    serializer_class = serializers.GroupLifeInsuranceSerializer


class GroupInsuranceBeneficiariesViewSet(viewsets.ModelViewSet):
    queryset = insuranceapp.GroupInsuranceBeneficiaries.objects.all()
    serializer_class = serializers.GroupInsuranceBeneficiariesSerializer


class TravelInsuranceEntryViewSet(viewsets.ModelViewSet):
    queryset = insuranceapp.TravelInsuranceEntry.objects.all()
    serializer_class = serializers.TravelInsuranceEntrySerializer
