from django.contrib.postgres.search import TrigramSimilarity
from django.db.models.functions import Cast
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
            "gender",
            "company_email",
            "job_titles",
            "job_title_description",
            "pager",
            "department",
            "unit",
            "branch",
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
            "company_id",
            "mobile_no",
            "company_email",
            "unique_code",
            "is_gm",
            "is_accountant",
            "is_super_hr",
            "is_hr",
            "is_super"
        ]


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = employee_model.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    filterset_class = EmployeeFilterSet


class EmployeeAppraisalViewSet(viewsets.ModelViewSet):
    queryset = employee_model.EmployeeAppraisal.objects.all()
    serializer_class = serializers.EmployeeAppraisalSerializer
    filterset_fields = "__all__"


# class SelfAppraisalResponseViewSet(viewsets.ModelViewSet):
#     queryset = employee_model.SelfAppraisalResponse.objects.all()
#     serializer_class = serializers.SelfAppraisalResponseSerializer


# class EmployeePromotionViewSet(viewsets.ModelViewSet):
#     queryset = employee_model.EmployeePromotion.objects.all()
#     serializer_class = serializers.EmployeePromotionSerializer


class EmployeeMedicalClaimViewSet(viewsets.ModelViewSet):
    queryset = employee_model.EmployeeMedicalClaim.objects.all()
    serializer_class = serializers.EmployeeMedicalClaimSerializer
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
    filterset_fields = [
        "id",
        "code",
        "name",
        "max_number_of_days",
    ]


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = employee_model.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    filterset_fields = ["id", "code", "name", "first_category_code", "company_id",]


class UnitViewSet(viewsets.ModelViewSet):
    queryset = employee_model.Unit.objects.all()
    serializer_class = serializers.UnitSerializer
    filterset_fields = [
        "id",
        "code",
        "name",
        "department",
        "company_id",
    ]


class BranchViewSet(viewsets.ModelViewSet):
    queryset = employee_model.Branch.objects.all()
    serializer_class = serializers.BranchSerializer
    filterset_fields = [
        "code",
        "name",
        "unit",
        "company_id",
    ]


class NotchViewSet(viewsets.ModelViewSet):
    queryset = employee_model.Notch.objects.all()
    serializer_class = serializers.NotchesSerializer
    filterset_fields = "__all__"


class AppraisalGradingViewSet(viewsets.ModelViewSet):
    queryset = employee_model.AppraisalGrading.objects.all()
    serializer_class = serializers.AppraisalGradingSerializer
    filterset_fields = [
        "id",
        "grade",
        "recommendation",
    ]


class PayGroupViewSet(viewsets.ModelViewSet):
    queryset = employee_model.PayGroup.objects.all()
    serializer_class = serializers.PayGroupSerializer
    filterset_fields = ["id", "no", "company", "total_medical_claim_amount", "comp_id"]


class EmployeeDeductionViewSet(viewsets.ModelViewSet):
    queryset = employee_model.EmployeeDeduction.objects.all()
    serializer_class = serializers.EmployeeDeductionSerializer
    filterset_fields = ["id", "employee", "employee_name"]


class KPIViewSet(viewsets.ModelViewSet):
    queryset = employee_model.KPI.objects.all()
    serializer_class = serializers.KPISerializer
    filterset_fields = "__all__"


class EmployeeKRAViewSet(viewsets.ModelViewSet):
    queryset = employee_model.EmployeeKRA.objects.all()
    serializer_class = serializers.EmployeeKRASerializer
    filterset_fields = "__all__"

class PropertyAssignmentViewSet(viewsets.ModelViewSet):
    queryset = employee_model.PropertyAssignment.objects.all()
    serializer_class = serializers.PropertyAssignmentSerializer
    filterset_fields = "__all__"


class PropertyRequestViewSet(viewsets.ModelViewSet):
    queryset = employee_model.PropertyRequest.objects.all()
    serializer_class = serializers.PropertyRequestSerializer
    filterset_fields = "__all__"


class SupervisorRatingGuideViewSet(viewsets.ModelViewSet):
    queryset = employee_model.SupervisorRatingGuide.objects.all()
    serializer_class = serializers.SupervisorRatingGuideSerializer
    filterset_fields = "__all__"


class BehaviourialRatingGuideViewSet(viewsets.ModelViewSet):
    queryset = employee_model.BehaviourialRatingGuide.objects.all()
    serializer_class = serializers.BehaviourialRatingGuideSerializer
    filterset_fields = "__all__"

class BehavourialCompetenciesViewSet(viewsets.ModelViewSet):
    queryset = employee_model.BehaviouralCompetencies.objects.all()
    serializer_class = serializers.BehaviourialCompetenciesSerializer
    filterset_fields = "__all__"


class EmployeeBehaviouralViewSet(viewsets.ModelViewSet):
    queryset = employee_model.EmployeeBehavioural.objects.all()
    serializer_class = serializers.EmployeeBehaviourialSerializer
    filterset_fields = "__all__"