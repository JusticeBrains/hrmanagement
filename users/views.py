from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .serializers import CustomUserSerializer

User = get_user_model()


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    filterset_fields = [
        "id",
        "username",
        "assigned_area",
        "email",
        "first_name",
        "last_name",
        "is_super",
        "is_hr",
        "is_active",
        "is_super_hr",
        "is_admin",
        "company",
        "staff_category",
        "employee_level",
        "emp_code",
        "is_verified",
        "unique_code",
        "is_accountant",
        "employee_id",
        "is_gm",
        "multiple_companies",
        "companies",
    ]
