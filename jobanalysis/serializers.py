from rest_framework import serializers

from . import models as jobanalysis_model


class JobAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = jobanalysis_model.JobAnalysis
        fields = "__all__"


class JobAnalysisDutiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = jobanalysis_model.JobAnalysisDuties
        fields = "__all__"


class JobRequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = jobanalysis_model.JobRequirements
        fields = "__all__"


class JobAnalysisSupervisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = jobanalysis_model.JobAnalysisSupervision
        fields = "__all__"


class JobAnalysisContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = jobanalysis_model.JobAnalysisContact
        fields = "__all__"


class JobAnalysisAuthorityuLimitSerializer(serializers.ModelSerializer):
    class Meta:
        model = jobanalysis_model.JobAnalysisAuthorityLimit
        fields = "__all__"


class JobAnalysisDemandSerializer(serializers.ModelSerializer):
    class Meta:
        model = jobanalysis_model.JobAnalysisDemand
        fields = "__all__"


class JobAnalysisRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = jobanalysis_model.JobAnalysisRequirement
        fields = "__all__"


class JobEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = jobanalysis_model.JobEvaluation
        fields = "__all__"