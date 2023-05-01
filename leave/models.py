from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime, timedelta
# from django.db.models import F
# from employee.models import Employee

from options import text_options
from django.utils import timezone

User = get_user_model()


class LeaveRequest(models.Model):
    leave_type = models.CharField(_("Leave Type"), max_length=50, null=True, blank=True)
    leave_description = models.CharField(
        _("Leave Description"), max_length=150, null=True, blank=True
    )
    start_date = models.DateField(
        _("From Date"), auto_now=False, auto_now_add=False, null=True, blank=True
    )
    no_of_days_requested = models.PositiveIntegerField(_("No Of Days Requested"))
    job_description = models.CharField(
        _("Job Description"), max_length=150, null=True, blank=True
    )
    job_title = models.CharField(_("Job Title"), max_length=50, null=True, blank=True)
    employee_unit = models.CharField(
        _("Employee Unit"), max_length=80, null=True, blank=True
    )
    employee_branch = models.CharField(
        _("Employee Branch"), max_length=150, null=True, blank=True
    )
    employee_level = models.CharField(
        _("Employee Level"), max_length=50, null=True, blank=True
    )
    date_applied = models.DateField(_("Date Applied"), default=timezone.now)
    status = models.CharField(_("Status"), max_length=150, null=True, blank=True)
    hod_status = models.CharField(
        _("HOD Status"), max_length=150, null=True, blank=True
    )
    hod_remarks = models.CharField(
        _("HOD Remarks"), max_length=250, null=True, blank=True
    )
    relieving_officer_name = models.CharField(
        _("Relieving Officer Name"), max_length=250, null=True, blank=True
    )
    hod_remarks_date = models.CharField(
        _("HOD Remarks Date"), blank=True, null=True
    )
    hr_status = models.CharField(_("HR Status"), max_length=50, null=True, blank=True)
    hr_remarks = models.CharField(_("HR Remarks"), max_length=50, null=True, blank=True)
    hr_remarks_date = models.CharField(_("HR Remarks Date"), blank=True, null=True)
    employee = models.ForeignKey("employee.Employee", verbose_name=_("Employee"), on_delete=models.CASCADE, null=True, blank=True)
    dep_code = models.CharField(
        _("Department Code"), max_length=50, null=True, blank=True
    )
    dep = models.CharField(_("Department"), max_length=50, null=True, blank=True)
    supporting_doc = models.TextField(_("Supporting Document"), null=True, blank=True)
    no_of_days_left = models.PositiveIntegerField(
        _("Number of Days Left"), editable=True, null=True, blank=True
    )
    emp_code = models.CharField(_("Employee Code"), max_length=50, null=True, blank=True)

    @property
    def end_date(self):
        current_date = datetime.now().date()
        start_date = max(self.start_date, current_date)
        days_added = 0

        while days_added < self.no_of_days_requested:
            start_date += timedelta(days=1)
            if start_date.weekday() >= 5:
                continue
            days_added += 1
        return start_date


    def clean(self):
        max_days = self.employee.staff_category_code.max_number_of_days

        # if self.employee.days_left is None:
        #     emp_days_left = 0
        # else:
        emp_days_left = self.employee.days_left

        if self.no_of_days_requested > emp_days_left:
            raise ValueError(
                f"Number of planned Days Exceed Maximum Days Left of {emp_days_left} "
            )
        
        if emp_days_left is not None:
            if self.no_of_days_requested <= emp_days_left:
                self.no_of_days_left = emp_days_left - self.no_of_days_requested

        if self.employee.no_of_days_exhausted == max_days:
            self.no_of_days_requested = 0
            self._meta.get_field("no_of_days_requested").editable = False
        else:
            self._meta.get_field("no_of_days_requested").editable = True



    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     # update employee days_left field after leave request is saved
    #     Employee.objects.filter(id=self.employee.id).update(
    #         days_left=self.no_of_days_left, no_of_days_exhausted=self.no_of_days_requested
    #     )

    class Meta:
        verbose_name = "Leave Request"
        verbose_name_plural = "Leave Requests"

    def __str__(self):
        return f"{self.leave_type}, {self.start_date} - {self.no_of_days_requested}"


class LeaveType(models.Model):
    code = models.UUIDField(
        _("Code"), primary_key=True, editable=False, default=uuid.uuid4
    )
    name = models.CharField(_("Name"), max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = "Leave Type"
        verbose_name_plural = "Leave Types"

    def __str__(self):
        return f"{self.code} - {self.name}"


class LeaveLimits(models.Model):
    code = models.UUIDField(
        _("Code"), primary_key=True, editable=False, default=uuid.uuid4
    )
    staff_category = models.CharField(
        _("Staff Category"), max_length=50, blank=True, null=True
    )
    leave_type = models.ForeignKey(
        "leave.LeaveType", verbose_name=_("Leave Type"), on_delete=models.CASCADE
    )
    no_of_days_allowed = models.PositiveIntegerField(
        _("No. Of Days Allowed"), blank=True, null=True
    )

    class Meta:
        verbose_name = "Leave Limits"
        verbose_name_plural = "Leave Limits"

    def __str__(self):
        return f"{self.leave_type} - {self.no_of_days_allowed}"
