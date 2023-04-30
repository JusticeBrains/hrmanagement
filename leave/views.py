from django_property_filter import PropertyDateFilter, PropertyFilterSet
from rest_framework import viewsets
from . import models as leavemodel

from .serializers import ( LeaveLimitsSerializer, 
                          LeaveRequestSerializer,
                          LeaveTypeSerializer,
                          )

class LeavePlanFilter(PropertyFilterSet):
    end_date = PropertyDateFilter(field_name='end_date')

    class Meta:
        model = leavemodel.LeaveRequest
        property_fields = [
            ('end_date',PropertyDateFilter,['exact', 'gt', 'gte']),
        ]
        fields = "__all__"

class LeaveRequestViewSet(viewsets.ModelViewSet):
    queryset = leavemodel.LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer
    filterset_class = LeavePlanFilter
    


class LeaveLimitsViewSet(viewsets.ModelViewSet):
    queryset = leavemodel.LeaveLimits.objects.all()
    serializer_class = LeaveLimitsSerializer


class LeaveTypeViewSet(viewsets.ModelViewSet):
    queryset = leavemodel.LeaveType.objects.all()
    serializer_class = LeaveTypeSerializer


