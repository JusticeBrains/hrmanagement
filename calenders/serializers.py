from rest_framework import serializers

from .models import Period


class PeriodSerializer(serializers.ModelSerializer):
    date = serializers.DateField()
    active = serializers.BooleanField()
    month = serializers.ReadOnlyField()
    year = serializers.ReadOnlyField()

    class Meta:
        model = Period
        fields = "__all__"

    @property
    def get_month(self, obj):
        return obj.date.month
    
    @property
    def get_year(self, obj):
        return obj.data.year