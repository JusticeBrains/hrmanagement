from rest_framework import viewsets

from .models import (
    EmployeeRequisition,
    ApplicantQualification,
    JobApplication,
    JobRequirements,
    Interview,
)

from .serializers import (
    EmployeeRequisitionSerializer,
    JobApplicationSerializer,
    JobRequirementSerializer,
    InterviewSerializer,
    ApplicantQualificationSerializer,
)


class EmployeeRequisitionViewSet(viewsets.ModelViewSet):
    queryset = EmployeeRequisition.objects.all()
    serializer_class = EmployeeRequisitionSerializer
    filterset_fields = ["id", "department", "position", "no_of_vacancies"]


class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    filterset_fields = ["id", "employee_requisition", "year"]



class JobRequirementsViewSet(viewsets.ModelViewSet):
    queryset = JobRequirements.objects.all()
    serializer_class = JobRequirementSerializer
    filterset_fields = ["id", "employee_requisition", "requirement_name"]


class InterviewscoreViewSet(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
    filterset_fields = ["id",'job_application', 'panelist_name']


class AppicantQualifivationViewSet(viewsets.ModelViewSet):
    queryset = ApplicantQualification.objects.all()
    serializer_class = ApplicantQualificationSerializer
    filterset_fields = ["id" ,"job_application"]
