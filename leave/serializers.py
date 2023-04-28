from datetime import datetime, timedelta
from rest_framework import serializers
from django_property_filter import PropertyDateFilter

from .models import (
    LeaveLedger,
    LeaveLimits,
    LeaveType,
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
    
    def get_end_date(self, obj):
        """custom method to compute duration"""
        current_date = datetime.now().date()
        start_date = max(obj.start_date, current_date)
        days_added = 0

        while days_added < obj.no_of_planned_days:
            start_date += timedelta(days=1)
            if start_date.weekday() >= 5:
                continue
            days_added += 1
        return start_date


class LeaveLimitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveLimits
        fields = "__all__"


class LeaveTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveType
        fields = "__all__"


class LeaveLedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveLedger
        fields = "__all__"