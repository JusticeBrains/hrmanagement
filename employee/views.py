from django.shortcuts import render

from django_property_filter import (
    PropertyFilterSet,
    PropertyNumberFilter,
    PropertyAllValuesFilter,
)
from rest_framework import viewsets
from . import models as employee_model
from . import serializers


class EmployeeFilterSet(PropertyFilterSet):
    fullname = PropertyAllValuesFilter(field_name="fullname")

    class Meta:
        model = employee_model.Employee
        property_fields = [
            (
                "fullname",
                PropertyAllValuesFilter,
                [
                    "exact",
                ],
            ),
        ]
        fields = [
            "code",
            "first_name",
            "last_name",
            "middle_name",
            "job_title",
            "gender",
            "company_email",
            "job_titles",
            "job_title_description",
            "pager",
            "first_category_level",
            "second_category_level",
            "third_category_level",
            "fourth_category_level",
            "fifth_category_level",
            "employment_date",
            "status",
            "termination_date",
            "employement_contract_code",
            "birth_date",
            "ssno",
            "pay_group_code",
            "salary_grade",
            "payment_mode",
            "payment_method",
            "days_left",
        ]


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = employee_model.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    filterset_class = EmployeeFilterSet


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


class EmployeePayReviewFilterSet(PropertyFilterSet):
    new_base_pay = PropertyNumberFilter(field_name="new_base_pay")

    class Meta:
        model = employee_model.EmployeePayReview
        property_fields = [
            ("new_base_pay", PropertyNumberFilter, ["lte", "gte"]),
        ]
        fields = "__all__"


class EmployeePayReviewViewSet(viewsets.ModelViewSet):
    queryset = employee_model.EmployeePayReview.objects.all()
    serializer_class = serializers.EmployeePayReviewSerializer
    filterset_class = EmployeePayReviewFilterSet


class StaffCategoryViewSet(viewsets.ModelViewSet):
    queryset = employee_model.StaffCategory.objects.all()
    serializer_class = serializers.StaffCategorySerializer
    filterset_fields = ['code', 'name', 'max_number_of_days',]

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = employee_model.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    filterset_fields = ['code', ]


class UnitViewSet(viewsets.ModelViewSet):
    queryset = employee_model.Unit.objects.all()
    serializer_class = serializers.UnitSerializer


class BranchViewSet(viewsets.ModelViewSet):
    queryset = employee_model.Branch.objects.all()
    serializer_class = serializers.BranchSerializer