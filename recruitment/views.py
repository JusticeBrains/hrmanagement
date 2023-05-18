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


class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer


class JobRequirementsViewSet(viewsets.ModelViewSet):
    queryset = JobRequirements.objects.all()
    serializer_class = JobRequirementSerializer

class InterviewscoreViewSet(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer


class AppicantViewSet(viewsets.ModelViewSet):
    queryset = ApplicantQualification.objects.all()
    serializer_class = ApplicantQualificationSerializer