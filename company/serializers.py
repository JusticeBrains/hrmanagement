import random
from rest_framework import serializers

from . import models as comp_models


class CompanySerializer(serializers.ModelSerializer):
    alias = serializers.SerializerMethodField()
    class Meta:
        model = comp_models.Company
        fields = "__all__"
    
    def get_alias(self, obj):
        return f"{obj.name[:3]}{random.randint(300,9000)}"


class CompanyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.CompanyType
        fields = "__all__"


class JobTitlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.JobTitles
        fields = "__all__"


class SalaryGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.SalaryGrade
        fields = "__all__"


class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.Holidays
        fields = "__all__"


class MedicalCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.MedicalCodes
        fields = "__all__"


class MedicalCentresSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.MedicalCentres
        fields = "__all__"


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.Property
        fields = "__all__"


class PropertyAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.PropertyAssignment
        fields = "__all__"


class DisciplinaryActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.DisciplinaryActions
        fields = "__all__"


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.Job
        fields = "__all__"


class HRNeedsLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.HRNeedsLine
        fields = "__all__"


class HRApprovalEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.HRApprovalEntry
        fields = "__all__"


class HRAlertsSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.HRAlerts
        fields = "__all__"


class WorkmenCompensationSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.WorkmenCompensation
        fields = "__all__"


class ExpatriatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.Expatriates
        fields = "__all__"


class ExpatriatesApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.ExpatriateApplication
        fields = "__all__"


class CompanyStaffBreakdownSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.CompanyStaffBreakdown
        fields = "__all__"


class PassportIssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.PassportIssues
        fields = "__all__"


class PerformanceOverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.PerformanceOverview
        fields = "__all__"


class OrganizationStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.OrganizationalStructure
        fields = "__all__"


class GrievanceHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.GrievanceHeader
        fields = "__all__"


class GrievanceLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.GrievanceLine
        fields = "__all__"


class GrievanceEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.GrievanceEntry
        fields = "__all__"


class GrievanceCommitteeMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.GrievanceCommitteMembers
        fields = "__all__"


class TravelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.Travels
        fields = "__all__"


class TravelExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.TravelExpenses
        fields = "__all__"


class CourierCompaniesSerilizer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.CourierCompanies
        fields = "__all__"


class CourierServiceRequisitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.CourierServiceRequisition
        fields = "__all__"


class HospitalityFacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.HospitalityFacilities
        fields = "__all__"


class HospitalityServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.HospitalityServices
        fields = "__all__"


class CollectiveBargainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.CollectiveBargaining
        fields = "__all__"


class CBAIssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.CBAIssues
        fields = "__all__"


class SJNCMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.SJNCMembers
        fields = "__all__"


class CashBenefitPaymentSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.CashBenefitPayments
        fields = "__all__"


class EndOfServiceEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.EndOfServiceEntry
        fields = "__all__"
