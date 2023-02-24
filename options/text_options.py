from django.db import models
from django.utils.translation import gettext_lazy as _


class GENDER(models.TextChoices):
    Male = "Male", _("Male")
    Female = "Female", _("Female")


class EMPLOYEESTATUS(models.TextChoices):
    ACTIVE = "ACTIVE", _("Active")
    INACTIVE = "INACTIVE", _("Inactive")
    TERMINATED = "TERMINATED", _("Terminated")


class MARITALSTATUS(models.TextChoices):
    MARRIED = "MARRIED", _("Married")
    DIVORCED = "DIVORCED", _("Divorced")
    SINGLE = "SINGLE", _("Single")
    SEPERATED = "SEPERATED", _("Seperated")
    WIDOWED = "WIDOWED", _("Widowed")
    NONE = "NONE", _("None")


class FREQUENCY(models.TextChoices):
    DAILY = "DAILY", _("Daily")
    WEEKLY = "WEEKLY", _("Weekly")
    MONTHLY = "MONTHLY", _("Monthly")
    QUARTERLY = "QUARTERLY", _("Quarterly")
    ANNUALLY = "ANNUALLY", _("Annually")
    IRREGULAR = "IRREGULAR", _("Irregular")
    INTERVAL = "INTERVAL", _("Interval")
    OTHER = "OTHER", _("Other")


class SUPERVISIONTYPE(models.TextChoices):
    SUPERVISION_GIVEN = "SUPERVISION GIVEN", _("Supervision Given")
    SUPERVISION_RECEIVED = "SUPERVISION RECEIVED", _("Supervision Received")


class MODEOFAPPOINTMENT(models.TextChoices):
    LOCAL = "LOCAL", _("Local")
    EXPARTRIATE = "EXPARTRIATE", _("Expartraite")


class CONTACTTYPE(models.TextChoices):
    INTERNAL = "INTERNAL", _("Internal")
    EXTERNAL = "EXTERNAL", _("External")


class DEMANDTYPE(models.TextChoices):
    PHYSICAL_WORK_ENVIRONMENT = "PHYSICAL WORK ENVIRONMENT", _("Physical Work Environment")
    PHYSICAL_EFFORT = "PHYSICAL EFFORT", _("Physical Effort")
    PSYCHOLOGICAL_DEMANDS = "Psychological Demands", _("Psychological Demands")


class REQUIREMENTTYPE(models.TextChoices):
    QUALIFICATION = "QUALIFICATION", _("Qualification")
    MINIMUM_EXPERIENCE = "MINIMUM EXPERIENCE", _("Minimum Experience")
    TECHNICAL_COMPETENCIES = "TECHNICAL COMPETENCIES", _("Technical Competencies")
    MANAGERIAL_COMPETENCIES = "MANAGERIAL COMPETENCIES", _("Managerial Competencies")
    PERSONAL_COMPETENCIES = "PERSONAL COMPETENCIES", _("Personal Competencies")


class ASSIGNEDAREA(models.TextChoices):
    GENERAL = "GENERAL", _("General")
    STAFFING = "STAFFING", _("Staffing")
    TRAINING = "TRAINING", _("Training")
    COMPENSATION = "COMPENSATION", _("Compensation")
    LEAVE = "LEAVE", _("Leave")
    MEDICALS = "MEDICALS", _("Medicals")
    LABOUR_RELATIONS = "LABOUR RELATIONS", _("Labour Relations")
    TRAVELS = "TRAVELS", _("Travels")
    SERVICES = "SERVICES", _("Services")


class LEAVEREQUESTSTATUS(models.TextChoices):
    APPROVED = "APPROVED", _("Approved")
    DEFERRED = "DEFERRED", _("Deferred")
    REJECTED = "REJECTED", _("Rejected")


class APPRAISALGRADES(models.TextChoices):
    POOR = "POOR", _("Poor")
    SATISFACTORY = "SATISFACTORY", _("Satisfactory")
    GOOD = "GOOD", _("Good")
    EXCELLENT = "EXCELLENT", _("Excellent")


class MEDICALLIMITTYPE(models.TextChoices):
    NO_LIMIT = "NO LIMIT", _("No Limit")
    PER_VISIT = "PER VISIT", _("Per Visit")
    ANNUAL = "Annual", _("Annual")


class MedicalType(models.TextChoices):
    CLAIM = "CLAIM", _("Claim")
    REFUND = "REFUND", _("Refund")


class EmployeeType(models.TextChoices):
    ACTIVE_EMPLOYEE = "ACTIVE EMPLOYEE", _("Active Employee")
    SERVICE_PERSONNEL = "SERVICE PERSONNEL", _("Service Personnel")
    RETIRED_EMPLOYEE = "Retired Employee", _("Retired Employee")
    ATTACHMENT = "ATTACHMENT", _("Attachment")


class OffenseType(models.TextChoices):
    MINOR = "MINOR", _("Minor")
    MAJOR = "MAJOR", _("Major")
    SERIOUS = "SERIOUS", _("Serious")


class RecommendedAction(models.TextChoices):
    QUERY = "QUERY", _("Query")
    VERBAL_WARNING = "VERBAL WARNING", _("Verbal Warning")
    WRITTENG_WARNING = "WRITTEN WARNING", _("Written Warning")
    SUSPENSION = "SUSPENSION", _("Suspension")
    DEMOTION = "DEMOTION", _("Demotion")
    TERMINATION = "TERMINATION", _("Termination")
    DISMISSAL = "DISMISSAL", _("Dismissal")


class TrainingType(models.TextChoices):
    IN_HOUSE = "IN HOUSE", _("In House")
    EXTERNAL = "EXTERNAL", _("External")
    OVERSEAS = "OVERSEAS", _("Overseas")


class TrainingSchedule(models.TextChoices):
    WEEKDAYS = "WEEKDAYS", _("Weekdays")
    WEEKDAYS_SATURDAYS = "WEEKDAYS + SATURDAYS", _("Weekdays + Saturdays")
    WEEKDAYS_WEEKENDS = "WEEKDAYS + WEEKENDS", _("WEEKDAYS + WEEKENDS")


class TrainingStatus(models.TextChoices):
    PLAN = "PLAN", _("Plan")
    SCHEDULED = "SCHEDULED", _("Scheduled")
    COMPLETED = "COMPLETED", _("Completed")
    CANCELLED = "CANCELLED", _("Cancelled")


class ExpenseType(models.TextChoices):
    PER_INDIVIDUAL = "PER INDIVIDUAL", _("Per Individual")
    TOTAL_COST = "TOTAL COST", _("Total Cost")


class RequestTrainingType(models.TextChoices):
    INTERNAL = "INTERNAL", _("Internal")
    EXTERNAL = "EXTERNAL", _("External")
    INTERNATIONAL = "INTERNATIONAL", _("International")


class TrainingRating(models.TextChoices):
    EXCELLENT = "EXCELLENT", _("Excellent")
    GOOD = "GOOD", _("Good")
    AVERAGE = "AVERAGE", _("Average")
    BELOW_AVERAGE = "BELOW AVERAGE", _("Below Average")
    POOR = "POOR", _("Poor")


class ExpenseUsageType(models.TextChoices):
    LOCAL = "LOCAL", _("Local")
    FOREIGN = "FOREIGN", _("Foreign")


class PublicationType(models.TextChoices):
    INTERNAL = "INTERNAL", _("Internal")
    EXTERNAL = "EXTERNAL", _("External")
    INTERNAL_EXTERNAL = "INTERNAL & EXTERNAL", _("Internal & External")


class QualificationType(models.TextChoices):
    INTERNAL = "INTERNAL", _("Internal")
    EXTERNAL = "EXTERNAL", _("External")
    PREVIOUS_POSITION = "PREVIOUS POSITION", _("Previous Position")


class TitleOption(models.TextChoices):
    MR = "MR.", _("Mr.")
    MISS = "MISS.", _("Miss.")
    MRS = "MRS.", _("Mrs.")
    DR = "DR.", _("Dr.")
    PROF = "PROF.", _("Prof")


class JobMedicals(models.TextChoices):
    NOT_PASSED = "NOT PASSED", _("Not Passed")
    PASSED = "PASSED", _("Passed")


class ApplicationStatus(models.TextChoices):
    APPLICANT = "APPLICANT", _("Applicant")
    INTERVIEWED_EXAMINED = "INTERVIEWED/EXAMINED", _("Interviewed/Examined")
    SHORT_LISTED = "SHORT_LISTED", _("Short Listed")
    SELECTED = "SELECTED", _("Selected")


class OverallStatus(models.TextChoices):
    NOT_RECOMMENDED = "NOT RECOMMENDED", _("Not Recommended")
    RECOMMENDED = "RECOMMENDED", _("Recommended")


class EmploymentStatus(models.TextChoices):
    OFFERED = "OFFERED", _("Offered")
    ACCEPTED = "ACCEPTED", _("Accepted")


class QualificationMetricOption(models.TextChoices):
    SKILLS = "SKILLS", _("Skills")
    QUALIFICATION = "QUALIFICATION", _("Qualification")
    EXPERIENCE = "EXPERIENCE", _("Experience")


class WorkmenOption(models.TextChoices):
    INCIDENT = "INCODENT", _("Incident")
    COMPENSATION_CLAIM = "COMPENSATION CLAIM", _("Compensation Claim")


class DocumentTypeOption(models.TextChoices):
    STAFFING = "STAFFING", _("Staffing")
    TRAINING = "TRAINING", _("Training")
    COMPENSATION = "COMPENSATION", _("Compensation")
    LEAVE = "LEAVE", _("Leave")
    MEDICALS = "MEDICALS", _("Medicals")
    LABOUR = "LABOUR", _("Labour")
    TRAVELS = "TRAVELS", _("Travels")
    SERVICES = "SERVICES", _("Services")


class DocumentStatus(models.TextChoices):
    CREATED = "CREATED", _("Created")
    OPEN = "OPEN", _("Open")
    CANCELED = "CANCELED", _("Canceled")
    REJECTED = "REJECTED", _("Rejected")
    APPROVED = "APPROVED", _("Approved")


class CompanyEmployeeType(models.TextChoices):
    GHANAIAN = "GHANAIAN", _("Ghanaian")
    EXPATRIATE = "EXPATRIATE", _("Expatriate")


class VisaType(models.TextChoices):
    SINGLE_ENTRY = "SINGLE ENTRY", _("Single Entry")
    MULTIPLE_ENTRY = "MULTIPLE ENTRY", _("Multiple Entry")


class PerformanceOverviewType(models.TextChoices):
    INITIAL_SETUP = "INITIAL SETUP", _("Initial Setup")
    INTERIM_REVIEW = "INTERIM REVIEW", _("Interim Review")
    YEAR_END_REVIEW = "YEAR ENDREVIEW", _("Year End REview")


class CorporateValuesType(models.TextChoices):
    VISION_MISSION = "VISION/MISSION", _("Vision/Mission")
    VALUES = "VALUES", _("Values")


class RatingResult(models.TextChoices):
    UNACCEPTABLE = "UNACCEPTABLE", _("Unacceptable")
    EXPECTATION = "EXPECTATION", _("Expectation")
    BELOW_EXPECTATIONS = "BELOW EXPECTATIONS", _("Below Expectations")
    AVERAGE_EXPECTATIONS = "AVERAGE EXPECTATIONS", _("Average Expectations")
    MEETS_EXPECTATIONS = "MEETS EXPECTATIONS", _("Meets Expectations")
    EXCEEDS_EXPECTATIONS = "EXCEEDS EXPECTATIONS", _("Exceeds Expectations")


class ReviewType(models.TextChoices):
    QUARTERLY_REVIEW = "QUARTERLY REVEIW", _("Quarterly Review")
    YEAR_END_REVIEW = "YEAR END REVIEW", _("Year End Review")
    YEAR_END_APPRAISAL = "YEAR END APPRAISAL", _("Year End Appraisal")


class InsuranceType(models.TextChoices):
    GROUP_PERSONAL = "GROUP PERSONAL", _("Group Personal")
    WORKMEN_COMPENSATION = "WORKMEN'S COMPENSATION", _("Workmen's Compensation")
    LIFE_INSURANCE = "LIFE INSURANCE", _("Life Insurance")
    FIRE_ALLIED_PERILS = "FIRE & ALLIED PERILS", _("Fire & Allied Perils")
    VERHICLE_INSURANCE = "VEHICLE INSURANCE", _("Vehicle Insurance")
    OTHERS = "OTHERS", _("Others")
    

class PersonnelType(models.TextChoices):
    STAFF = "STAFF", _("Staff")
    NON_STAFF = "NON STAFF", _("Non Staff")


class EndOfServiceOptions(models.TextChoices):
    RETIREMENT_BENEFIT = "RETIREMENT BENEFIT", _("Retirement Benefit")
    LONG_SERVICE = "LONG SERVICE", _("Long Service")