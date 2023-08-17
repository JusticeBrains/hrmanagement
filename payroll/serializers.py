from rest_framework import serializers

from .models import Transactions, SavingScheme, SavingSchemeEntries, TransactionEntries


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = "__all__"


class SavingSchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingScheme
        fields = "__all__"


class SavingSchemeEntriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingSchemeEntries
        fields = "__all__"


class TransactionEntriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionEntries
        fields = "__all__"
