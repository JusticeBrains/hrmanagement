from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from options import text_options

User = get_user_model()


class CorporateValues(models.Model):
    header_no = models.CharField(_("Header No."), max_length=50)
    entry_no = models.PositiveIntegerField(_("Entry No."))
    entry_type = models.CharField(_("Entry Type"), choices=text_options.CorporateValuesType.choices, max_length=50)
    department_code = models.ForeignKey("company.Department", verbose_name=_("Department Code"),
                                        on_delete=models.CASCADE)
    department_name = models.CharField(_("Department Name"), max_length=50)
    departmental_vision = models.CharField(_("Departmental Vision"), max_length=250)
    departmental_mission = models.CharField(_("Departmental Mission"), max_length=250)
    departmental_values = models.CharField(_("Departmental Values"), max_length=250)
    last_date_modified = models.DateField(_("Date Modified"), auto_now=True, auto_now_add=False)
    user_id = models.ForeignKey(User, verbose_name=_("User ID"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Corporate Values"
        verbose_name_plural = "Corporate Values"

    def __str__(self):
        return self.departmental_values


class CooperateObjectives(models.Model):
    code = models.CharField(_("Code"), max_length=50)
    objective_description = models.CharField(_("Objective Description"), max_length=250)
    year_of_review = models.PositiveIntegerField(_("Year Of Review"))
    start_date = models.DateField(_("Start Date"), auto_now=True, auto_now_add=False)
    end_date = models.DateField(_("End Date"), auto_now=True, auto_now_add=False)
    transaction_date = models.DateField(_("Transaction Date"), auto_now=True, auto_now_add=False)
    user_id = models.ForeignKey(User, verbose_name=_("User ID"), on_delete=models.CASCADE)
    posted = models.BooleanField(_("Posted"))

    class Meta:
        verbose_name = "Cooperate Objectives"
        verbose_name_plural = "Cooperate Objectives"

    def __str__(self):
        return self.code


class DepartmentalObjectives(models.Model):
    corp_obj_code = models.ForeignKey("CooperateObjectives", verbose_name=_("Cooperate Objective Code"),
                                      on_delete=models.CASCADE)
    corp_obj_description = models.CharField(_("Corp Objective Description"), max_length=250)
    entry_no = models.PositiveIntegerField(_("Entry No."))
    department_code = models.ForeignKey("company.Department", verbose_name=_("Department Code"),
                                        on_delete=models.CASCADE)
    department_name = models.CharField(_("Department Name"), max_length=150)
    objective_description = models.CharField(_("Objective Description"), max_length=250)
    review_year = models.PositiveIntegerField(_("Review Year"))
    start_date = models.DateField(_("Start Date"), auto_now=True, auto_now_add=False)
    end_date = models.DateField(_("End Date"), auto_now=True, auto_now_add=False)
    posted = models.BooleanField(_("Posted"))
    transaction_date = models.DateField(_("Transaction Date"), auto_now=True, auto_now_add=False)
    user_id = models.ForeignKey(User, verbose_name=_("User ID"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Departmental Objectives"
        verbose_name_plural = "Departmental Objectives"

    def __str__(self):
        return self.objective_description


class ObjectiveReviewLines(models.Model):
    header_no = models.CharField(_("Header No"), max_length=50)
    entry_no = models.PositiveIntegerField(_("Entry No."))
    performance_target = models.CharField(_("Performance Target"), max_length=250)
    corporate_objective_code = models.ForeignKey("CooperateObjectives", verbose_name=_("Corporate Objective Code"),
                                                 on_delete=models.CASCADE)
    departmental_objective = models.ForeignKey("DepartmentalObjectives", verbose_name=_("Depatmental Objective Text"),
                                               on_delete=models.CASCADE)
    measurement_indicator = models.CharField(_("Measurement Indicator"), max_length=250)
    weight = models.DecimalField(_("Weight"), max_digits=5, decimal_places=2)
    target_date = models.DateField(_("Target Date"), auto_now=True, auto_now_add=False)
    rating = models.PositiveIntegerField(_("Rating"))
    rating_results = models.CharField(_("Rating Result"), choices=text_options.RatingResult.choices, max_length=50)
    remarks = models.CharField(_("Remarks"), max_length=250)
    achievements = models.CharField(_("Achievements"), max_length=50)

    class Meta:
        verbose_name = "Objective Review Lines"
        verbose_name_plural = "Objective Review Lines"

    def __str__(self):
        return self.remarks


class IndividualObjectiveLines(models.Model):
    header_no = models.CharField(_("Header No."), max_length=50)
    entry_no = models.PositiveIntegerField(_("Entry No."))
    performance_target = models.CharField(_("Performance Target"), max_length=250)
    corporate_objective_code = models.ForeignKey("CooperateObjectives", verbose_name=_("Corporate Objective Code"),
                                                 on_delete=models.CASCADE)
    dept_objective_entry_no = models.PositiveIntegerField(_("Departmental Objective Entry No,"))
    dept_object_text = models.ForeignKey("DepartmentalObjectives", verbose_name=_("Departmental Objective Text"),
                                         on_delete=models.CASCADE)
    measurement_indicator = models.CharField(_("Measurement Indicator"), max_length=50)
    weight = models.DecimalField(_("Weight"), max_digits=5, decimal_places=2)
    target_date = models.DateField(_("Target Date"), auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = "Individual Objective Lines"
        verbose_name_plural = "Individual Objective Lines"

    def __str__(self):
        return f"{self.dept_object_text}"


class IndividualObjectiveBase(models.Model):
    no = models.CharField(_("No."), max_length=50)
    department_code = models.ForeignKey("company.Department", verbose_name=_("Department Code"),
                                        on_delete=models.CASCADE)
    department_name = models.CharField(_("Department Name"), max_length=50)
    performance_start_date = models.DateField(_("Performance Start Date"), auto_now=True, auto_now_add=False)
    performance_end_date = models.DateField(_("Performance End Date"), auto_now=True, auto_now_add=False)
    emp_code = models.ForeignKey("employee.Employee", verbose_name=_("Employee Code"), on_delete=models.CASCADE)
    job_title = models.CharField(_("Job Title"), max_length=50)
    employment_date = models.DateField(_("Employment Date"), auto_now=True, auto_now_add=False)
    supervisor_level = models.CharField(_("Supervisor Level"), max_length=150)
    supervisor_name = models.CharField(_("Supervisor Name"), max_length=150)
    supervisor_job_title = models.CharField(_("Supervisor Job Title"), max_length=50)
    next_supervisor_level = models.CharField(_("Supervisor Level"), max_length=150)
    next_supervisor_name = models.CharField(_("Next Supervisor Name"), max_length=150)
    next_supervisor_job_title = models.CharField(_("Next Supervisor Job Title"), max_length=50)
    employee_signed = models.BooleanField(_("Employee Signed"))
    employee_signed_date = models.DateField(_("Employee Signed Date"), auto_now=True, auto_now_add=False)
    supervisor_signed = models.BooleanField(_("Supervisor Signed"))
    supervisor_signed_date = models.DateField(_("Supervisor Signed Date"), auto_now=True, auto_now_add=False)
    next_supervisor_signed = models.BooleanField(_("Next Supervisor Signed"))
    next_supervisor_signed_date = models.DateField(_("Next Supervisor Signed Date"), auto_now=True, auto_now_add=False)
    transation_date = models.DateField(_("Transaction Date"), auto_now=True, auto_now_add=False)
    user_id = models.CharField(_("User ID"), max_length=50)

    class Meta:
        abstract = True


class IndividualObjectiveSetting(IndividualObjectiveBase):
    posted = models.BooleanField(_("Posted"))
    final_review_complete = models.BooleanField(_("Final Review Complete"))
    total_individual_weights = models.DecimalField(_("Total Individual Weights"), max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "Individual Objective Setting"
        verbose_name_plural = "Individual Objective Settings"

    def __str__(self):
        return self.final_review_complete


class IndividualObjectiveReview(IndividualObjectiveBase):
    emp_name = models.CharField(_("Employee Name"), max_length=150)
    objective_setting_no = models.ForeignKey("IndividualObjectiveSetting", verbose_name=_("Objective Setting Number"),
                                             on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Individual Objective Review"
        verbose_name_plural = "Individual Objective Reviews"

    def __str__(self):
        return self.emp_name
