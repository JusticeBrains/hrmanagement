from . import models as comp_models
from . import serializers
from django_property_filter import PropertyFilterSet, PropertyAllValuesFilter
from rest_framework import viewsets


class CompanyFilterSet(PropertyFilterSet):
    alias = PropertyAllValuesFilter(field_name="alias")
    
    class Meta:
        model = comp_models.Company
        fields = ['id', 'name', 'comp_type']



class CompanyViewSet(viewsets.ModelViewSet):
    queryset = comp_models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
    filterset_class = CompanyFilterSet

class CompanyTypeViewSet(viewsets.ModelViewSet):
    queryset = comp_models.CompanyType.objects.all()
    serializer_class = serializers.CompanyTypeSerializer


class JobTitleViewSet(viewsets.ModelViewSet):
    queryset = comp_models.JobTitles.objects.all()
    serializer_class = serializers.JobTitlesSerializer
    filterset_fields = ['id','code','payroll_structure', 'salary_grade', 'description']


class SalaryGradeViewSet(viewsets.ModelViewSet):
    queryset = comp_models.SalaryGrade.objects.all()
    serializer_class = serializers.SalaryGradeSerializer
    filterset_fields = ['id','code','payroll_structure', 'job_titles', 'transport_rate']



class HolidayViewSet(viewsets.ModelViewSet):
    queryset = comp_models.Holidays.objects.all()
    serializer_class = serializers.HolidaySerializer


class MedicalCodesViewSet(viewsets.ModelViewSet):
    queryset = comp_models.MedicalCodes.objects.all()
    serializer_class = serializers.MedicalCodesSerializer


class MedicalCentreViewSet(viewsets.ModelViewSet):
    queryset = comp_models.MedicalCentres.objects.all()
    serializer_class = serializers.MedicalCentresSerializer


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = comp_models.Property.objects.all()
    serializer_class = serializers.PropertySerializer


class PropertyAssignmentViewSet(viewsets.ModelViewSet):
    queryset = comp_models.PropertyAssignment.objects.all()
    serializer_class = serializers.PropertyAssignmentSerializer


class DiscplinaryActionsViewSet(viewsets.ModelViewSet):
    queryset = comp_models.DisciplinaryActions.objects.all()
    serializer_class = serializers.DisciplinaryActionsSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = comp_models.Job.objects.all()
    serializer_class = serializers.JobSerializer


class MinimumQualificationViewSet(viewsets.ModelViewSet):
    queryset = comp_models.MinimumQualification.objects.all()
    serializer_class = serializers.MinimumQualificationSerializer


class JobOpeningViewSet(viewsets.ModelViewSet):
    queryset = comp_models.JobOpening.objects.all()
    serializer_class = serializers.JonOpeningSerializer


class ApplicationPoolViewSet(viewsets.ModelViewSet):
    queryset = comp_models.ApplicationPool.objects.all()
    serializer_class = serializers.ApplicationPoolSerializer



class ApplicationReferencesViewSet(viewsets.ModelViewSet):
    queryset = comp_models.ApplicationReferences.objects.all()
    serializer_class = serializers.ApplicationReferencesSeriailizer


class ApplicationQEViewSet(viewsets.ModelViewSet):
    queryset = comp_models.ApplicationQE.objects.all()
    serializer_class = serializers.ApplicationQESerializer



class JobApplicationQualificationViewSet(viewsets.ModelViewSet):
    queryset = comp_models.JobApplicationQualification.objects.all()
    serializer_class = serializers.JobApplicationQualificationSerializer



class HRNeedsLineViewSet(viewsets.ModelViewSet):
    queryset = comp_models.HRNeedsLine.objects.all()
    serializer_class = serializers.HRNeedsLineSerializer


class HRApprovalEntryViewSet(viewsets.ModelViewSet):
    queryset = comp_models.HRApprovalEntry.objects.all()
    serializer_class = serializers.HRApprovalEntrySerializer


class HRAlertsViewSet(viewsets.ModelViewSet):
    queryset = comp_models.HRAlerts.objects.all()
    serializer_class = serializers.HRAlertsSerializer


class WorkmenCompensationViewSet(viewsets.ModelViewSet):
    queryset = comp_models.WorkmenCompensation.objects.all()
    serializer_class = serializers.WorkmenCompensationSerializer


class ExpatriatesViewSet(viewsets.ModelViewSet):
    queryset = comp_models.Expatriates.objects.all()
    serializer_class = serializers.ExpatriatesSerializer


class ExpatriatesApplicationViewSet(viewsets.ModelViewSet):
    queryset = comp_models.ExpatriateApplication.objects.all()
    serializer_class = serializers.ExpatriatesApplicationSerializer


class CompanyStaffBreakdownViewSet(viewsets.ModelViewSet):
    queryset = comp_models.CompanyStaffBreakdown.objects.all()
    serializer_class = serializers.CompanyStaffBreakdownSerializer


class PassportIssuesViewSet(viewsets.ModelViewSet):
    queryset = comp_models.PassportIssues.objects.all()
    serializer_class = serializers.PassportIssuesSerializer


class PerformanceOverviewViewSet(viewsets.ModelViewSet):
    queryset = comp_models.PerformanceOverview.objects.all()
    serializer_class = serializers.PerformanceOverviewSerializer


class OrganizationStructureViewSet(viewsets.ModelViewSet):
    queryset = comp_models.OrganizationalStructure.objects.all()
    serializer_class = serializers.OrganizationStructureSerializer


class GrievanceHeaderViewSet(viewsets.ModelViewSet):
    queryset = comp_models.GrievanceHeader.objects.all()
    serializer_class = serializers.GrievanceHeaderSerializer


class GrievanceLineViewSet(viewsets.ModelViewSet):
    queryset = comp_models.GrievanceLine.objects.all()
    serializer_class = serializers.GrievanceLineSerializer


class GrievanceEntryViewSet(viewsets.ModelViewSet):
    queryset = comp_models.GrievanceEntry.objects.all()
    serializer_class = serializers.GrievanceEntrySerializer


class GrievanceCommitteeMembersViewSet(viewsets.ModelViewSet):
    queryset = comp_models.GrievanceCommitteMembers.objects.all()
    serializer_class = serializers.GrievanceCommitteeMembersSerializer


class TravelsViewSet(viewsets.ModelViewSet):
    queryset = comp_models.Travels.objects.all()
    serializer_class = serializers.TravelsSerializer


class TravelExpensesViewSet(viewsets.ModelViewSet):
    queryset = comp_models.TravelExpenses.objects.all()
    serializer_class = serializers.TravelExpensesSerializer


class CourierCompaniesViewSet(viewsets.ModelViewSet):
    queryset = comp_models.CourierCompanies.objects.all()
    serializer_class = serializers.CourierCompaniesSerilizer


class CourierServiceRequisitionViewset(viewsets.ModelViewSet):
    queryset = comp_models.CourierServiceRequisition.objects.all()
    serializer_class = serializers.CourierServiceRequisitionSerializer


class HospitalityFacilitiesViewSet(viewsets.ModelViewSet):
    queryset = comp_models.HospitalityFacilities.objects.all()
    serializer_class = serializers.HospitalityFacilitiesSerializer


class HospitalityServicesViewSet(viewsets.ModelViewSet):
    queryset = comp_models.HospitalityServices.objects.all()
    serializer_class = serializers.HospitalityServicesSerializer


class CollectiveBargainingViewSet(viewsets.ModelViewSet):
    queryset = comp_models.CollectiveBargaining.objects.all()
    serializer_class = serializers.CollectiveBargainingSerializer


class CBAIssuesViewSet(viewsets.ModelViewSet):
    queryset = comp_models.CBAIssues.objects.all()
    serializer_class = serializers.CBAIssuesSerializer


class SJNCMembersViewSet(viewsets.ModelViewSet):
    queryset = comp_models.SJNCMembers.objects.all()
    serializer_class = serializers.SJNCMembersSerializer


class CashBenefitPaymentViewSet(viewsets.ModelViewSet):
    queryset = comp_models.CashBenefitPayments.objects.all()
    serializer_class = serializers.CashBenefitPaymentSerilaizer


class EndOfServiceEntryViewSet(viewsets.ModelViewSet):
    queryset = comp_models.EndOfServiceEntry.objects.all()
    serializer_class = serializers.EndOfServiceEntrySerializer
