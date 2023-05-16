from rest_framework import serializers
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


class EmployeePromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee_model.EmployeePromotion
        fields = "__all__"


class EmployeeMedicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee_model.EmployeeMedicals
        fields = "__all__"


class EmployeeDisciplinaryActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee_model.EmployeeDisciplinaryActions
        fields = "__all__"


class EmployeePayReviewSerializer(serializers.ModelSerializer):
    new_base_pay = serializers.SerializerMethodField()
    class Meta:
        model = employee_model.EmployeePayReview
        fields = ['no', 'review_type','emp_code', 'emp_name', 'job_title_code', 'job_title', 'base_pay', 'new_base_pay']


class StaffCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =employee_model.StaffCategory
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

class PayCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee_model.PayCategoryList
        fields = "__all__"


class AppraisalGradingSerializer(serializers.ModelSerializer):
    score_range = IntegerRangeField()
    class Meta:
        model = employee_model.AppraisalGrading
        fields = ['id','score_range', 'grade', 'recommendation']


class EmployeeAppraisalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee_model.EmployeeAppraisalDetail
        fields = "__all__"