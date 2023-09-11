from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db import transaction
User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    company_names = serializers.ReadOnlyField()
    class Meta:
        model = User
        exclude = ['user_permissions', 'groups','is_superuser','last_login', 'date_joined',]

    def create(self, validated_data):
        # Perform the user creation logic
        user = User.objects.create(**validated_data)

        # Update the company_names field
        if user.companies.exists():
            company_dicts = []
            related_companies = user.companies.all()

            for company in related_companies:
                company_dicts.append({"company_id": str(company.id), "name": company.name})

            with transaction.atomic():
                user.company_names = [{"companies": company_dicts}]
                user.save()

        return user