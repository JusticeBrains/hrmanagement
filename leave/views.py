from django.shortcuts import render

from rest_framework import viewsets
from . import models as leavemodel

from .serializers import (LeavePlanSerializer,
                          LeaveRequestSerializer,
                          LeaveTransactionSerializer,
                          PolicySerializer,
                          AssignmentSerializer
                          )


class LeavePlanViewSet(viewsets.ModelViewSet):
    queryset = leavemodel.LeavePlan.objects.all()
    serializer_class = LeavePlanSerializer


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
