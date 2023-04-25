from rest_framework import serializers
from . import models as employee_model


class EmployeeSerializer(serializers.ModelSerializer):
    fullname = serializers.SerializerMethodField()
    class Meta:
        model = employee_model.Employee
        fields = "__all__"


class AppraisalAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee_model.AppraisalAreas
        fields = "__all__"


class EmployeeAppraisalSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee_model.EmployeeAppraisal
        fields = "__all__"


class EmployeeAppraisalResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee_model.EmployeeAppraisalResponse
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


class EmployeePolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = employee_model.EmployeePolicy
        fields = "__all__"

class EmployeePayReviewSerializer(serializers.ModelSerializer):
    new_base_pay = serializers.SerializerMethodField()
    class Meta:
        model = employee_model.EmployeePayReview
        fields = ['no', 'review_type','emp_code', 'emp_name', 'job_title_code', 'job_title', 'base_pay', 'new_base_pay']
    