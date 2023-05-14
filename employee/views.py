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
            "id",
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

class EmployeeAppraisalViewSet(viewsets.ModelViewSet):
    queryset = employee_model.EmployeeAppraisal.objects.all()
    serializer_class = serializers.EmployeeAppraisalSerializer
    filterset_fields = ["id","emp_name", 'employee_code', "job_title", "appraiser", "department", "grade", "performance_score", "percentage_score", "period"]


# class SelfAppraisalResponseViewSet(viewsets.ModelViewSet):
#     queryset = employee_model.SelfAppraisalResponse.objects.all()
#     serializer_class = serializers.SelfAppraisalResponseSerializer


class EmployeePromotionViewSet(viewsets.ModelViewSet):
    queryset = employee_model.EmployeePromotion.objects.all()
    serializer_class = serializers.EmployeePromotionSerializer


class EmployeeMedicalViewSet(viewsets.ModelViewSet):
    queryset = employee_model.EmployeeMedicals.objects.all()
    serializer_class = serializers.EmployeeMedicalSerializer
    filterset_fields = "__all__"


class EmployeeDisciplinaryActionViewSet(viewsets.ModelViewSet):
    queryset = employee_model.EmployeeDisciplinaryActions.objects.all()
    serializer_class = serializers.EmployeeDisciplinaryActionsSerializer
    filterset_fields = "__all__"


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
    filterset_fields = ['code', 'name', 'first_category_code' ]


class UnitViewSet(viewsets.ModelViewSet):
    queryset = employee_model.Unit.objects.all()
    serializer_class = serializers.UnitSerializer
    filterset_fields = ['code', 'name', 'second_category_code',]



class BranchViewSet(viewsets.ModelViewSet):
    queryset = employee_model.Branch.objects.all()
    serializer_class = serializers.BranchSerializer
    filterset_fields = ['code', 'name', 'third_category_code',]



class NotchViewSet(viewsets.ModelViewSet):
    queryset = employee_model.Notch.objects.all()
    serializer_class = serializers.NotchesSerializer


class PayCategoryListViewSet(viewsets.ModelViewSet):
    queryset = employee_model.PayCategoryList.objects.all()
    serializer_class = serializers.PayCategoryListSerializer


class EmployeeAppraisalDetailViewSet(viewsets.ModelViewSet):
    queryset = employee_model.EmployeeAppraisalDetail.objects.all()
    serializer_class = serializers.EmployeeAppraisalDetailSerializer
    filterset_fields = ["id","employee_appraisal", "emp_code", "period", "score",'kpi_appraisal_area', 'employee_id']


class AppraisalGradingViewSet(viewsets.ModelViewSet):
    queryset = employee_model.AppraisalGrading.objects.all()
    serializer_class = serializers.AppraisalGradingSerializer