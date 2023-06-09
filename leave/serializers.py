from datetime import date, datetime, timedelta, time
from django.forms import ValidationError
from rest_framework import serializers
from django_property_filter import PropertyDateFilter
from django.utils import timezone

from .models import (
    HolidayCalender,
    LeaveType,
    LeaveRequest,
    LeavePlan
)

class DateOnlyField(serializers.ReadOnlyField):
    def to_representation(self, value):
        return value.strftime('%Y-%m-%d')
    

class LeaveRequestSerializer(serializers.ModelSerializer):
    start_date = serializers.CharField(required=False)
    end_date = serializers.ReadOnlyField()
    resumption_date = serializers.ReadOnlyField()
    extension_date = serializers.ReadOnlyField()
    no_of_days_requested = serializers.IntegerField(required=False)
    no_of_extension_days = serializers.IntegerField(required=False)




    @property
    def get_end_date(self, obj):
        holidays = HolidayCalender.objects.values_list("holiday_date", flat=True)
        current_date = datetime.now().date()
        start_date = max(obj.start_date, current_date)
        days_added = 0

        while days_added < obj.no_of_days_requested:
            start_date += timedelta(days=1)
            if start_date.weekday() >= 5 or start_date in holidays:
                continue
            days_added += 1
        print(type(start_date))
        return start_date


    @property
    def get_extension_date(self, obj):
        holidays = HolidayCalender.objects.values_list("holiday_date", flat=True)
        current_date = datetime.now().date()
        start_date = obj.end_date
        start_date = max(start_date, current_date)
        days_added = 0

        while days_added < obj.no_of_extension_days:
            start_date += timedelta(days=1)
            if start_date.weekday() >= 5 or start_date in holidays:
                continue
            days_added += 1
        print(type(start_date))
        return start_date
    

    class Meta:
        model = LeaveRequest
        fields = "__all__"




class LeavePlanSerializer(serializers.ModelSerializer):
    start_date = serializers.CharField(required=False)
    end_date = serializers.ReadOnlyField()
    resumption_date = serializers.ReadOnlyField()
    no_of_days_requested = serializers.IntegerField(required=False)


    @property
    def get_end_date(self, obj):
        holidays = HolidayCalender.objects.values_list("holiday_date", flat=True)
        current_date = datetime.now().date()
        start_date = max(obj.start_date, current_date)
        days_added = 0

        while days_added < obj.no_of_days_requested or start_date in holidays:
            start_date += timedelta(days=1)
            if start_date.weekday() >= 5:
                continue
            days_added += 1
        print(type(start_date))
        return start_date
    
    # def get_plan_days_left(self, obj):
    #     employee = obj.employee
    #     max_days = obj.leave_type.calculate_max_days(employee)
    #     emp_days_left = employee.plan_days_left
    #     if employee.plan_days_left is not None:
    #         if obj.no_of_days_requested > emp_days_left:
    #             raise serializers.ValidationError("error")
    #     return emp_days_left - obj.no_of_days_requested

    # def validate(self, data):
    #     if data['employee'].plan_days_left is not None:
    #         if data['no_of_days_requested'] > data['employee'].plan_days_left:
    #             raise ValidationError("Number of planned days exceed maximum days left")
            
    #     return data   
    # start_date = serializers.DateField()
    # end_date = serializers.SerializerMethodField()
    
    class Meta:
        model = LeavePlan
        fields = "__all__"

    # def get_end_date(self, obj):
    #     """custom method to compute duration"""
    #     current_date = datetime.now().date()
    #     start_date = max(obj.start_date, current_date)
    #     days_added = 0

    #     while days_added < obj.no_of_days_requested:
    #         start_date += timedelta(days=1)
    #         if start_date.weekday() >= 5:
    #             continue
    #         days_added += 1
    #     return start_date


class LeaveTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveType
        fields = "__all__"

class HolidayCalenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidayCalender
        fields = "__all__"

