from rest_framework import serializers, exceptions
from . import models as employee_model
from drf_extra_fields.fields import IntegerRangeField


class EmployeeSerializer(serializers.ModelSerializer):
    fullname = serializers.SerializerMethodField()

    class Meta:
        model = employee_model.Employee
        fields = "__all__"

    def get_fullname(self, obj):
        if obj.middle_name:
            return f"{obj.last_name}, {obj.first_name} {obj.middle_name}"
        return f"{obj.last_name}, {obj.first_name}"


class EmployeeAppraisalSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee_model.EmployeeAppraisal
        fields = "__all__"


# class EmployeePromotionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = employee_model.EmployeePromotion
#         fields = "__all__"


class EmployeeMedicalClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee_model.EmployeeMedicalClaim
        fields = "__all__"


class EmployeeDisciplinaryActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee_model.EmployeeDisciplinaryActions
        fields = "__all__"


class EmployeePayReviewSerializer(serializers.ModelSerializer):
    new_base_pay = serializers.SerializerMethodField()

    class Meta:
        model = employee_model.EmployeePayReview
        fields = [
            "no",
            "review_type",
            "emp_code",
            "emp_name",
            "job_title_code",
            "job_title",
            "base_pay",
            "new_base_pay",
        ]


class StaffCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = employee_model.StaffCategory
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee_model.Department
        fields = "__all__"


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee_model.Unit
        fields = "__all__"


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee_model.Branch
        fields = "__all__"


class NotchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee_model.Notch
        fields = "__all__"


class AppraisalGradingSerializer(serializers.ModelSerializer):
    score_range = IntegerRangeField()
    company = serializers.ReadOnlyField()

    class Meta:
        model = employee_model.AppraisalGrading
        fields = [
            "id",
            "score_range",
            "grade",
            "recommendation",
            "company",
            "company_id",
        ]


class PayGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee_model.PayGroup
        fields = "__all__"


class EmployeeDeductionSerializer(serializers.ModelSerializer):
    employee_name = serializers.ReadOnlyField()

    class Meta:
        model = employee_model.EmployeeDeduction
        fields = "__all__"


class KPIValidator:
    def __call__(self, attrs):
        score = attrs["score"]
        kpi_score = attrs["kpi_score"]
        if score > kpi_score:
            raise exceptions.ValidationError("Score cannot be greater than KPI score.")
        return attrs


class KPISerializer(serializers.ModelSerializer):
    company = serializers.CharField(read_only=True)
    score = serializers.DecimalField(max_digits=5, decimal_places=2, read_only=True)
    kpi_score = serializers.DecimalField(max_digits=5, decimal_places=2, required=False)
    supervisor_score = serializers.DecimalField(
        max_digits=5, decimal_places=2, required=False
    )
    emp_score = serializers.DecimalField(max_digits=5, decimal_places=2, required=False)
    period = serializers.ReadOnlyField()

    class Meta:
        model = employee_model.KPI
        fields = "__all__"
        # validators = [KPIValidator()]


class EmployeeKRAValidator:
    def __call__(self, attrs):
        kpis = attrs["kpis"]
        total_score = attrs["total_score"]
        kpi_scores_sum = sum(kpi["kpi_score"] for kpi in kpis)
        if kpi_scores_sum != total_score:
            raise exceptions.ValidationError(
                "Sum of KPI scores must equal total score."
            )
        return attrs


class EmployeeKRASerializer(serializers.ModelSerializer):
    # # kpis = KPISerializer(many=True, write_only=True)
    # computed_supervisor_score = serializers.ReadOnlyField()
    # computed_employee_score = serializers.ReadOnlyField()
    class Meta:
        model = employee_model.EmployeeKRA
        fields = "__all__"
        # validators = [EmployeeKRAValidator()]

    # def create(self, validated_data):
    #     kpis_data = validated_data.pop("kpis")
    #     kpi = employee_model.EmployeeKRA.objects.create(**validated_data)
    #     for kpi_data in kpis_data:
    #         # employee_kra=self.id
    #         # kpi_appraisal_area = kpi_data["kpi_appraisal_area"]
    #         # kpi_appraisal_area_description = kpi_data["kpi_appraisal_area_description"]
    #         # score = kpi_data["score"]
    #         # emp_comment = kpi_data["emp_comment"]
    #         employee_id = kpi_data["employee_id"]
    #         # emp_code = kpi_data["emp_code"]
    #         # emp_name = kpi_data["emp_name"]
    #         # appraiser = kpi_data["appraiser"]
    #         # status = kpi_data["status"]
    #         # due_date = kpi_data["due_date"]
    #         # department = kpi_data["department"]
    #         # company = kpi_data["company"]
    #         kpi_score = kpi_data["kpi_score"]
    #         kpi.create_kpis(
    #             # kpi_appraisal_area,
    #             # kpi_appraisal_area_description,
    #             kpi_score,
    #             # score,
    #             # emp_comment,
    #             employee_id,
    #             # emp_code,
    #             # emp_name,
    #             # appraiser,
    #             # status,
    #             # due_date,
    #             # department,
    #             # company,
    #         )
    #     return kpi


class PropertyAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee_model.PropertyAssignment
        fields = "__all__"


class PropertyRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee_model.PropertyRequest
        fields = "__all__"


class SupervisorRatingGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee_model.SupervisorRatingGuide
        fields = "__all__"


class BehaviourialRatingGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee_model.BehaviourialRatingGuide
        fields = "__all__"


class BehaviourialCompetenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee_model.BehaviouralCompetencies
        fields = "__all__"

class EmployeeBehaviourialSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee_model.EmployeeBehavioural
        fields = "__all__"