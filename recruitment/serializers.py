from rest_framework import serializers
from .models import (
    EmployeeRequisition,
    JobApplication,
    ApplicantQualification,
    Interview,
)


class EmployeeRequisitionSerializer(serializers.ModelSerializer):
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