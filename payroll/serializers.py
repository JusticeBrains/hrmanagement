from rest_framework import serializers

from .models import Transactions, SavingScheme


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = "__all__"


class SavingSchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingScheme
        fields = "__all__"
