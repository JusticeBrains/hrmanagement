from rest_framework import viewsets

from .models import (
    CompanyMajors,
    EmployeeRequisition,
    ApplicantQualification,
    GlobalMajors,
    GlobalQualification,
    JobApplication,
    Interview,
    CompanyQualifications,
)

from .serializers import (
    CompanyMajorsSerializer,
    CompanyQualificationsSerializer,
    EmployeeRequisitionSerializer,
    GlobalMajorsSerializer,
    GlobalQualificationSerializer,
    JobApplicationSerializer,
    InterviewSerializer,
    ApplicantQualificationSerializer,
)


class EmployeeRequisitionViewSet(viewsets.ModelViewSet):
    queryset = EmployeeRequisition.objects.all()
    serializer_class = EmployeeRequisitionSerializer
    filterset_fields = [
        "id",
        "department",
        "position",
        "no_of_vacancies",
        "status",
        "published",
        "company",
        "company_id",
        "unique_code",
    ]


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
        "system_shortlisted",
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


class GlobalQualificationViewSet(viewsets.ModelViewSet):
    queryset = GlobalQualification.objects.all()
    serializer_class = GlobalQualificationSerializer
    filterset_fields = "__all__"


class CompanyQualificationsViewSet(viewsets.ModelViewSet):
    queryset = CompanyQualifications.objects.all()
    serializer_class = CompanyQualificationsSerializer
    filterset_fields = "__all__"


class GlobalMajorsViewSet(viewsets.ModelViewSet):
    queryset = GlobalMajors.objects.all()
    serializer_class = GlobalMajorsSerializer
    filterset_fields = "__all__"


class CompanyMajorsViewSet(viewsets.ModelViewSet):
    queryset = CompanyMajors.objects.all()
    serializer_class = CompanyMajorsSerializer
    filterset_fields = "__all__"
