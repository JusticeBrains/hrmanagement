import datetime
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db.models import Sum
from recruitment.models import (
    ApplicantQualification,
    CompanyQualifications,
    EmployeeRequisition,
    Interview,
    JobApplication,
)


@receiver(post_save, sender=Interview)
def update_total_interview_score(sender, instance, **kwargs):
    """
    Update total interview score of the applicant
    """
    post_save.disconnect(update_total_interview_score, sender=Interview)
    if instance.interview_score:
        applicant_id = JobApplication.objects.get(id=instance.job_application.id)
        total_score = Interview.objects.filter(job_application=applicant_id).aggregate(
            total_score=Sum("interview_score")
        )["total_score"]
        applicant_id.total_interview_score = (
            total_score if total_score is not None else None
        )
        applicant_id.save()
    post_save.connect(update_total_interview_score, sender=Interview)


@receiver(pre_save, sender=ApplicantQualification)
def populate_company_field_application(sender, instance, **kwargs):
    """
    Populate company field with company name from the job application
    """
    if instance:
        if instance.job_application:
            instance.company = instance.job_application.company


@receiver(pre_save, sender=EmployeeRequisition)
def populate_company_field_requistion(sender, instance, **kwargs):
    """
    Populate company field with company name from the job application
    """
    if instance:
        if instance.department:
            instance.company = instance.department.company
            instance.company_id = instance.department.company_id
            instance.qualifications = instance.company_qualifications.qualification_name


@receiver(pre_save, sender=JobApplication)
def system_shortlist(sender, instance, **kwargs):
    if instance:
        age = datetime.date.today().year - instance.date_of_brith.year
        years_of_experiences = (
            EmployeeRequisition.get_years_of_experience_for_shortlisting(
                instance.years_of_experience
            )
        )
        age_limit = EmployeeRequisition.get_age_for_shortlisting(age)
        instance.age = age
        application_qualification_value = (
            instance.company_qualifications.global_qualification.value
        )
        requistion_value = (
            instance.employee_requisition.company_qualifications.global_qualification.value
        )
        if (years_of_experiences and age_limit) is not None and (
            application_qualification_value >= requistion_value
        ):
            instance.system_shortlisted = True
        else:
            instance.system_shortlisted = False

        if instance.employee_requisition:
            instance.company = instance.employee_requisition.company
            instance.company_id = instance.employee_requisition.company_id
            instance.qualifications = instance.company_qualifications.qualification_name


@receiver(pre_save, sender=CompanyQualifications)
def populate_qualification_name(sender, instance, **kwargs):
    if instance:
        # qualifications = CompanyQualifications.objects.filter(
        #     id__in=[q for q in instance.globalqualification])
        instance.qualification_name = instance.global_qualification.name
        instance.company_name = instance.company.name
