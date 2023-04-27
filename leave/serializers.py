from rest_framework import serializers
from django_property_filter import PropertyDateFilter

from .models import (
    Policy,
    Assignment,
    LeaveRequest,
    LeaveTransaction,
    LeavePlan
)


class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = "__all__"


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = "__all__"


class LeaveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = "__all__"


class LeaveTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveTransaction
        fields = "__all__"


class LeavePlanSerializer(serializers.ModelSerializer):
    end_date = serializers.SerializerMethodField()
    class Meta:
        model = LeavePlan
        fields = "__all__"
