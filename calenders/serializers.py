from rest_framework import serializers

from .models import Period, PeriodYear, GlobalInputs


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        exclude = ["month_calendar"]

class PeriodYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodYear
        fields = "__all__"

class GlobalInputsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalInputs
        fields = "__all__"
    