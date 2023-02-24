from rest_framework import serializers
from . import models as training_model


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = training_model.Course
        fields = "__all__"


class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = training_model.CourseDetail
        fields = "__all__"


class OrganizerSerailizer(serializers.ModelSerializer):
    class Meta:
        model = training_model.Organizers
        fields = "__all__"


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = training_model.Plan
        fields = "__all__"


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = training_model.Expense
        fields = "__all__"


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = training_model.Budget
        fields = "__all__"


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = training_model.Request
        fields = "__all__"


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = training_model.Feedback
        fields = "__all__"


class ParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = training_model.Participants
        fields = "__all__"
