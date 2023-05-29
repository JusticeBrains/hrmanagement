from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum
from recruitment.models import Interview, JobApplication

@receiver(post_save, sender=Interview)
def update_total_interview_score(sender, instance, **kwargs):
    """
    Update total interview score of the applicant
    """
    post_save.disconnect(update_total_interview_score, sender=Interview)
    if instance.interview_score:
        applicant_id = JobApplication.objects.get(id=instance.job_application.id)
        total_score = Interview.objects.filter(job_application=applicant_id).aggregate(total_score=Sum('interview_score'))['total_score']
        applicant_id.total_interview_score  = total_score if total_score is not None else None
        applicant_id.save()
    post_save.connect(update_total_interview_score, sender=Interview)
    