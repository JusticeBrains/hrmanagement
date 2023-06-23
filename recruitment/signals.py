from datetime import datetime
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db.models import Sum
from recruitment.models import (
    ApplicantQualification,
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


@receiver(post_save, sender=ApplicantQualification)
def populate_company_field_application(sender, instance, **kwargs):
    """
    Populate company field with company name from the job application
    """
    post_save.disconnect(
        populate_company_field_application, sender=ApplicantQualification
    )
    if instance.job_application:
        instance.company = instance.job_application.company
        instance.save()
    post_save.connect(populate_company_field_application, sender=ApplicantQualification)


@receiver(post_save, sender=EmployeeRequisition)
def populate_company_field_requistion(sender, instance, **kwargs):
    """
    Populate company field with company name from the job application
    """
    post_save.disconnect(populate_company_field_requistion, sender=EmployeeRequisition)
    if instance.department:
        instance.company = instance.department.company
        instance.company_id = instance.department.company_id
        instance.save()
    post_save.connect(populate_company_field_requistion, sender=EmployeeRequisition)


@receiver(pre_save, sender=JobApplication)
def get_years_of_experience(sender, instance, **kwargs):
    years_of_experiences = EmployeeRequisition.get_years_of_experience_for_shortlisting(
        instance.years_of_experience
    )

    if instance:
        age = datetime.date() - instance.date_of_brith
        age_limit = EmployeeRequisition.get_age_for_shortlisting(age)
        if years_of_experiences:
            if (
                instance.years_of_experience in years_of_experiences.years_of_experience
                and age in age_limit
            ):
                instance.system_shortlisted = True
        if instance.employee_requisition:
            instance.company = instance.employee_requisition.company
            instance.company_id = instance.employee_requisition.company_id
