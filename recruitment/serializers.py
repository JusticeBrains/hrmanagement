from rest_framework import serializers
from .models import (
    CompanyQualifications,
    EmployeeRequisition,
    GlobalQualification,
    JobApplication,
    ApplicantQualification,
    Interview,
)
from drf_extra_fields.fields import IntegerRangeField


class EmployeeRequisitionSerializer(serializers.ModelSerializer):
    age_limits = IntegerRangeField()
    years_of_experience = IntegerRangeField()
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