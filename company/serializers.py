import random
from rest_framework import serializers

from . import models as comp_models


class CompanySerializer(serializers.ModelSerializer):
    alias = serializers.SerializerMethodField()
    class Meta:
        model = comp_models.Company
        fields = "__all__"
    
    def get_alias(self, obj):
        return f"{obj.name[:3]}{random.randint(300,9000)}"


class CompanyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.CompanyType
        fields = "__all__"


class JobTitlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.JobTitles
        fields = "__all__"


class SalaryGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.SalaryGrade
        fields = "__all__"


class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.Holidays
        fields = "__all__"


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.Job
        fields = "__all__"



