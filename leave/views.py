from django_property_filter import PropertyDateFilter, PropertyFilterSet
from rest_framework import viewsets
from . import models as leavemodel

from .serializers import (LeaveLedgerSerializer, LeaveLimitsSerializer, LeavePlanSerializer,
                          LeaveRequestSerializer,
                          LeaveTransactionSerializer, LeaveTypeSerializer,
                          PolicySerializer,
                          AssignmentSerializer
                          )

class LeavePlanFilter(PropertyFilterSet):
    end_date = PropertyDateFilter(field_name='end_date')

    class Meta:
        model = leavemodel.LeavePlan
        property_fields = [
            ('end_date',),
        ]
        fields = ['end_date',]

class LeavePlanViewSet(viewsets.ModelViewSet):
    queryset = leavemodel.LeavePlan.objects.all()
    serializer_class = LeavePlanSerializer
    filterset_class = LeavePlanFilter


class LeaveRequestViewSet(viewsets.ModelViewSet):
    queryset = leavemodel.LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer


class LeaveTransactionViewSet(viewsets.ModelViewSet):
    queryset = leavemodel.LeaveTransaction.objects.all()
    serializer_class = LeaveTransactionSerializer


class PolicyViewSet(viewsets.ModelViewSet):
    queryset = leavemodel.Policy.objects.all()
    serializer_class = PolicySerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = leavemodel.Assignment.objects.all()
    serializer_class = AssignmentSerializer


class LeaveLimitsViewSet(viewsets.ModelViewSet):
    queryset = leavemodel.LeaveLimits.objects.all()
    serializer_class = LeaveLimitsSerializer


class LeaveTypeViewSet(viewsets.ModelViewSet):
    queryset = leavemodel.LeaveType.objects.all()
    serializer_class = LeaveTypeSerializer


class LeaveLedgerViewSet(viewsets.ModelViewSet):
    queryset = leavemodel.LeaveLedger.objects.all()
    serializer_class = LeaveLedgerSerializer