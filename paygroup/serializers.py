from .models import PayGroup

from rest_framework import serializers


class PayGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayGroup
        fields = "__all__"
