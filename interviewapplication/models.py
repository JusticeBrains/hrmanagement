from django.db import models
from django.utils.translation import gettext_lazy as _


class InterviewScoreGuide(models.Model):
    weight = models.PositiveIntegerField(_("Weight"))
    minimum_score = models.DecimalField(_("Minimum Score"), max_digits=5, decimal_places=2)
    maximum_score = models.DecimalField(_("Maximum Score"), max_digits=5, decimal_places=2)

    class Meta:
        abstract = True


class InterviewScore(InterviewScoreGuide):
    publication_code = models.ForeignKey("company.JobOpening", verbose_name=_("Publication Code"),
                                         on_delete=models.CASCADE)
    entry_no = models.PositiveIntegerField(_("Entry No"))
    question_no = models.PositiveIntegerField(_("Question No."))
    question = models.CharField(_("Question"), max_length=150)
    score = models.DecimalField(_("Score"), max_digits=5, decimal_places=2)
    weight_average_score = models.DecimalField(_("Weighted Average Score"), max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "Interview / Test Score"
        verbose_name_plural = "Interview / Test Scores"

    def __str__(self):
        return self.score


class InterviewTestQuestionnaire(InterviewScoreGuide):
    publication_no = models.ForeignKey("company.JobOpening", verbose_name=_("Publication No."),
                                       on_delete=models.CASCADE)
    line_no = models.PositiveIntegerField(_("Line No."))
    question = models.CharField(_("Question"), max_length=150)

    class Meta:
        verbose_name = "Interview/Test Questionnaire"
        verbose_name_plural = "Interview/Test Questionnaires"

    def __str__(self):
        return f"{self.question}, {self.id}"


class InterviewPanel(models.Model):
    interview_no = models.CharField(_("Interview No."), max_length=50)
    entry_no = models.PositiveIntegerField(_("Entry No."))
    emp_code = models.ForeignKey("employee.Employee", verbose_name=_("Employee Code"), on_delete=models.CASCADE)
    interviewer_name = models.CharField(_("Interviewer Name"), max_length=150)
    job_title_code = models.ForeignKey("company.Job", verbose_name=_("Job Title Code"), on_delete=models.CASCADE)
    job_title = models.CharField(_("Job Title"), max_length=50)

    class Meta:
        verbose_name = "Interview Panel"
        verbose_name_plural = "Interview Panels"

    def __str__(self):
        return self.interviewer_name


class MedicalQuestionnaire(models.Model):
    publication_no = models.ForeignKey("company.JobOpening", verbose_name=_("Publication No."),
                                       on_delete=models.CASCADE)
    test_no = models.PositiveIntegerField(_("Test No."))
    medical_test = models.CharField(_("Medical Test"), max_length=150)

    class Meta:
        verbose_name = "Medical Questionnaire"
        verbose_name_plural = "Medical Questionnaires"

    def __str__(self):
        return self.medical_test


class ApplicantMedicalTest(models.Model):
    publication_no = models.ForeignKey("company.JobOpening", verbose_name=_("Publication No."),
                                       on_delete=models.CASCADE)
    entry_no = models.PositiveIntegerField(_("Entry No."))
    test_no = models.PositiveIntegerField(_("Test No."))
    medical_test = models.CharField(_("Medical Test"), max_length=150)
    passed = models.BooleanField(_("Passed"))

    class Meta:
        verbose_name = "Applicant Medical Test"
        verbose_name_plural = "Applicant Medical Tests"

    def __str__(self):
        return self.passed
