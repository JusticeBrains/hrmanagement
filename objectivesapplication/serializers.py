from rest_framework import serializers

from . import models as obje_model


class CorporateValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = obje_model.CooperateObjectives
        fields = "__all__"


class CooperateObjectivesSerializer(serializers.ModelSerializer):
    class Meta:
        model = obje_model.CooperateObjectives
        fields = "__all__"


class DepartmentObjectivesSerializer(serializers.ModelSerializer):
    class Meta:
        model = obje_model.DepartmentalObjectives
        fields = "__all__"


class ObjectiveReviewLinesSerilizer(serializers.ModelSerializer):
    class Meta:
        model = obje_model.ObjectiveReviewLines
        fields = "__all__"


class IndividualObjectiveLinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = obje_model.IndividualObjectiveLines
        fields = "__all__"


class IndividualObjectiveSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = obje_model.IndividualObjectiveSetting
        fields = "__all__"


class IndividualObjectiveReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = obje_model.IndividualObjectiveReview
        fields = "__all__"
