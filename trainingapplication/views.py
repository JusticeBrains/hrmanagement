from rest_framework import viewsets

from . import models as training_model
from . import serializers


class CourseViewSet(viewsets.ModelViewSet):
    queryset = training_model.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class CourseDetailViewSet(viewsets.ModelViewSet):
    queryset = training_model.CourseDetail.objects.all()
    serializer_class = serializers.CourseDetailSerializer


class OrganizerViewSet(viewsets.ModelViewSet):
    queryset = training_model.Organizers.objects.all()
    serializer_class = serializers.OrganizerSerailizer


class PlanViewSet(viewsets.ModelViewSet):
    queryset = training_model.Plan.objects.all()
    serializer_class = serializers.PlanSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = training_model.Expense.objects.all()
    serializer_class = serializers.ExpenseSerializer


class BudgteViewSet(viewsets.ModelViewSet):
    queryset = training_model.Budget.objects.all()
    serializer_class = serializers.BudgetSerializer


class RequestViewSet(viewsets.ModelViewSet):
    queryset = training_model.Request.objects.all()
    serializer_class = serializers.RequestSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = training_model.Feedback.objects.all()
    serializer_class = serializers.FeedbackSerializer


class ParticipantsViewSet(viewsets.ModelViewSet):
    queryset = training_model.Participants.objects.all()
    serializer_class = serializers.ParticipantsSerializer
