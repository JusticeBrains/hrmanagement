from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db import transaction

User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    company_names = serializers.ReadOnlyField()

    class Meta:
        model = User
        exclude = [
            "user_permissions",
            "groups",
            "is_superuser",
            "last_login",
            "date_joined",
        ]

    def create(self, validated_data):
        companies_data = validated_data.pop("companies", [])  # Extract companies data
        user = User.objects.create(**validated_data)

        if companies_data:
            user.companies.set(
                companies_data
            )  # Use set() to update the many-to-many relationship

            company_dicts = [
                {"company_id": str(company.id), "name": company.name}
                for company in companies_data
            ]

            with transaction.atomic():
                user.company_names = [{"companies": company_dicts}]
                user.save()

        return user