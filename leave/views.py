from django_property_filter import PropertyDateFilter, PropertyFilterSet
from rest_framework import viewsets
from . import models as leavemodel

from .serializers import (
    HolidayCalenderSerializer,
    LeaveRequestSerializer,
    LeaveTypeSerializer,
    LeavePlanSerializer
)


class LeaveRequestFilter(PropertyFilterSet):
    end_date = PropertyDateFilter(field_name="end_date")
    extension_date = PropertyDateFilter(field_name="extension_date")

    class Meta:
        model = leavemodel.LeaveRequest
        property_fields = [
            ("end_date", PropertyDateFilter, ["exact", "gt", "gte"]),
            ("extension_date", PropertyDateFilter, ["exact", "gt", "gte"]),
        ]
        fields = [
            "id",
            "leave_type",
            "start_date",
            "no_of_days_requested",
            "job_description",
            "job_title",
            "hod_status",
            "hod_remarks",
            "relieving_officer_name",
            'hr_status',
            'hr_remarks',
            'dep_code',
            'no_of_days_left',
            'emp_code',
            'status',
            'extension_status',
            'company',
            "unique_code",
            "unpaid_leave",
            "dep"
        ]


class LeaveRequestViewSet(viewsets.ModelViewSet):
    queryset = leavemodel.LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer
    filterset_class = LeaveRequestFilter


class LeavePlanFilter(PropertyFilterSet):
    end_date = PropertyDateFilter(field_name="end_date")

    class Meta:
        model = leavemodel.LeavePlan
        property_fields = [
            ("end_date", PropertyDateFilter, ["exact", "gt", "gte"]),
        ]
        fields = [
            "id",
            "leave_type",
            "start_date",
            "no_of_days_requested",
            "job_description",
            "job_title",
            "hod_status",
            "hod_remarks",
            "relieving_officer_name",
            'hr_status',
            'hr_remarks',
            'dep_code',
            'no_of_days_left',
            'emp_code',
            'status',
            'company',
            "unique_code",
            "employee"
        ]


class LeavePlanViewSet(viewsets.ModelViewSet):
    queryset = leavemodel.LeavePlan.objects.all()
    serializer_class = LeavePlanSerializer
    filterset_class = LeavePlanFilter


# class LeaveLimitsViewSet(viewsets.ModelViewSet):
#     queryset = leavemodel.LeaveLimits.objects.all()
#     serializer_class = LeaveLimitsSerializer


class LeaveTypeViewSet(viewsets.ModelViewSet):
    queryset = leavemodel.LeaveType.objects.all()
    serializer_class = LeaveTypeSerializer
    filterset_fields = "__all__"


class HolidayCalenderViewset(viewsets.ModelViewSet):
    queryset = leavemodel.HolidayCalender.objects.all()
    serializer_class = HolidayCalenderSerializer
    filterset_fields = "__all__"