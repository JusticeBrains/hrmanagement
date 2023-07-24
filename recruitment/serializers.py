from rest_framework import serializers
from .models import (
    CompanyMajors,
    CompanyQualifications,
    EmployeeRequisition,
    GlobalMajors,
    GlobalQualification,
    JobApplication,
    ApplicantQualification,
    Interview,
)
from drf_extra_fields.fields import IntegerRangeField


class EmployeeRequisitionSerializer(serializers.ModelSerializer):
    age_limits = IntegerRangeField()
    years_of_experience = IntegerRangeField()
    company_majors_array = serializers.ListField(
        child=serializers.CharField(required=False), allow_empty=True
    )

    class Meta:
        model = EmployeeRequisition
        fields = "__all__"


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = "__all__"


class ApplicantQualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantQualification
        fields = "__all__"


class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = "__all__"


class GlobalQualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalQualification
        fields = "__all__"


class CompanyQualificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyQualifications
        fields = "__all__"


class GlobalMajorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalMajors
        fields = "__all__"


class CompanyMajorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyMajors
        fields = "__all__"
