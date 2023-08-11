from . import models as comp_models
from . import serializers
from django_property_filter import PropertyFilterSet, PropertyAllValuesFilter
from rest_framework import viewsets


class CompanyFilterSet(PropertyFilterSet):
    alias = PropertyAllValuesFilter(field_name="alias")

    class Meta:
        model = comp_models.Company
        fields = ["id", "name", "comp_type"]


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = comp_models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
    filterset_class = CompanyFilterSet


class CompanyTypeViewSet(viewsets.ModelViewSet):
    queryset = comp_models.CompanyType.objects.all()
    serializer_class = serializers.CompanyTypeSerializer


class JobTitleViewSet(viewsets.ModelViewSet):
    queryset = comp_models.JobTitles.objects.all()
    serializer_class = serializers.JobTitlesSerializer
    filterset_fields = "__all__"


class SalaryGradeViewSet(viewsets.ModelViewSet):
    queryset = comp_models.SalaryGrade.objects.all()
    serializer_class = serializers.SalaryGradeSerializer
    filterset_fields = "__all__"


class HolidayViewSet(viewsets.ModelViewSet):
    queryset = comp_models.Holidays.objects.all()
    serializer_class = serializers.HolidaySerializer
    filterset_fields = "__all__"


class BankViewSet(viewsets.ModelViewSet):
    queryset = comp_models.Bank.objects.all()
    serializer_class = serializers.BankSerializer
    filterset_fields = "__all__"


class BankBranchViewSet(viewsets.ModelViewSet):
    queryset = comp_models.BankBranch.objects.all()
    serializer_class = serializers.BankBranchSerializer
    filterset_fields = "__all__"