from rest_framework import viewsets

from .models import (
    EmployeeRequisition,
    ApplicantQualification,
    JobApplication,
    Interview,
)

from .serializers import (
    EmployeeRequisitionSerializer,
    JobApplicationSerializer,
    InterviewSerializer,
    ApplicantQualificationSerializer,
)


class EmployeeRequisitionViewSet(viewsets.ModelViewSet):
    queryset = EmployeeRequisition.objects.all()
    serializer_class = EmployeeRequisitionSerializer
    filterset_fields = "__all__"


class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    filterset_fields = [
        "id",
        "employee_requisition",
        "year",
        "applicant_firstname",
        "applicant_lastname",
        "applicant_othername",
        "status",
        "total_interview_score",
        "recruited",
        "interviewed",
        "short_list",
        "company",
    ]


class InterviewscoreViewSet(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
    filterset_fields = [
        "id",
        "job_application",
        "panelist_name",
        "interview_location",
        "interview_score",
        "company",
    ]


class AppicantQualifivationViewSet(viewsets.ModelViewSet):
    queryset = ApplicantQualification.objects.all()
    serializer_class = ApplicantQualificationSerializer
    filterset_fields = ["id", "job_application", "qualification_name", "company"]
