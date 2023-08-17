from rest_framework import serializers

from .models import Period, PeriodYear


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = "__all__"

class PeriodYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodYear
        fields = "__all__"