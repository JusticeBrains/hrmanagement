from rest_framework import serializers

from . import models as comp_models


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.Company
        fields = "__all__"


class CompanyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.CompanyType
        fields = "__all__"


class CompanyFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.CompanyField
        fields = "__all__"


# class DepartmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = comp_models.Department
#         fields = "__all__"


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


class MinimumQualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.MinimumQualification
        fields = "__all__"


class QualificationMetricSQEFSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.QualificationMetricSQEF
        fields = "__all__"


class JonOpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.JobOpening
        fields = "__all__"


class ApplicationPoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.ApplicationPool
        fields = "__all__"


class ShortListedApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.ShortListedApplication
        fields = "__all__"


class ApplicationReferencesSeriailizer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.ApplicationReferences
        fields = "__all__"


class ApplicationQESerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.ApplicationQE
        fields = "__all__"


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.JobApplication
        fields = "__all__"


class JobApplicationQualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.JobApplicationQualification
        fields = "__all__"


class HRNeedsSQEFSerializer(serializers.ModelSerializer):
    class Meta:
        model = comp_models.HRNeedsSQEF
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
