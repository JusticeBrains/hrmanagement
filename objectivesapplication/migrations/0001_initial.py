# Generated by Django 4.1.7 on 2023-02-21 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0002_initial'),
        ('employee', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CooperateObjectives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, verbose_name='Code')),
                ('objective_description', models.CharField(max_length=250, verbose_name='Objective Description')),
                ('year_of_review', models.PositiveIntegerField(verbose_name='Year Of Review')),
                ('start_date', models.DateField(auto_now=True, verbose_name='Start Date')),
                ('end_date', models.DateField(auto_now=True, verbose_name='End Date')),
                ('transaction_date', models.DateField(auto_now=True, verbose_name='Transaction Date')),
                ('no_series', models.CharField(max_length=50, verbose_name='No. Series')),
                ('posted', models.BooleanField(verbose_name='Posted')),
            ],
            options={
                'verbose_name': 'Cooperate Objectives',
                'verbose_name_plural': 'Cooperate Objectives',
            },
        ),
        migrations.CreateModel(
            name='CorporateValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_no', models.CharField(max_length=50, verbose_name='Header No.')),
                ('entry_no', models.PositiveIntegerField(verbose_name='Entry No.')),
                ('entry_type', models.CharField(choices=[('VISION/MISSION', 'Vision/Mission'), ('VALUES', 'Values')], max_length=50, verbose_name='Entry Type')),
                ('department_name', models.CharField(max_length=50, verbose_name='Department Name')),
                ('departmental_vision', models.CharField(max_length=250, verbose_name='Departmental Vision')),
                ('departmental_mission', models.CharField(max_length=250, verbose_name='Departmental Mission')),
                ('departmental_values', models.CharField(max_length=250, verbose_name='Departmental Values')),
                ('last_date_modified', models.DateField(auto_now=True, verbose_name='Date Modified')),
            ],
            options={
                'verbose_name': 'Corporate Values',
                'verbose_name_plural': 'Corporate Values',
            },
        ),
        migrations.CreateModel(
            name='DepartmentalObjectives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corp_obj_description', models.CharField(max_length=250, verbose_name='Corp Objective Description')),
                ('entry_no', models.PositiveIntegerField(verbose_name='Entry No.')),
                ('department_name', models.CharField(max_length=150, verbose_name='Department Name')),
                ('objective_description', models.CharField(max_length=250, verbose_name='Objective Description')),
                ('review_year', models.PositiveIntegerField(verbose_name='Review Year')),
                ('start_date', models.DateField(auto_now=True, verbose_name='Start Date')),
                ('end_date', models.DateField(auto_now=True, verbose_name='End Date')),
                ('posted', models.BooleanField(verbose_name='Posted')),
                ('transaction_date', models.DateField(auto_now=True, verbose_name='Transaction Date')),
                ('corp_obj_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objectivesapplication.cooperateobjectives', verbose_name='Cooperate Objective Code')),
                ('department_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.department', verbose_name='Department Code')),
            ],
            options={
                'verbose_name': 'Departmental Objectives',
                'verbose_name_plural': 'Departmental Objectives',
            },
        ),
        migrations.CreateModel(
            name='ObjectiveReviewLines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_no', models.CharField(max_length=50, verbose_name='Header No')),
                ('entry_no', models.PositiveIntegerField(verbose_name='Entry No.')),
                ('performance_target', models.CharField(max_length=250, verbose_name='Performance Target')),
                ('measurement_indicator', models.CharField(max_length=250, verbose_name='Measurement Indicator')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Weight')),
                ('target_date', models.DateField(auto_now=True, verbose_name='Target Date')),
                ('rating', models.PositiveIntegerField(verbose_name='Rating')),
                ('rating_results', models.CharField(choices=[('UNACCEPTABLE', 'Unacceptable'), ('EXPECTATION', 'Expectation'), ('BELOW EXPECTATIONS', 'Below Expectations'), ('AVERAGE EXPECTATIONS', 'Average Expectations'), ('MEETS EXPECTATIONS', 'Meets Expectations'), ('EXCEEDS EXPECTATIONS', 'Exceeds Expectations')], max_length=50, verbose_name='Rating Result')),
                ('remarks', models.CharField(max_length=250, verbose_name='Remarks')),
                ('achievements', models.CharField(max_length=50, verbose_name='Achievements')),
                ('corporate_objective_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objectivesapplication.cooperateobjectives', verbose_name='Corporate Objective Code')),
                ('departmental_objective', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objectivesapplication.departmentalobjectives', verbose_name='Depatmental Objective Text')),
            ],
            options={
                'verbose_name': 'Objective Review Lines',
                'verbose_name_plural': 'Objective Review Lines',
            },
        ),
        migrations.CreateModel(
            name='IndividualObjectiveSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=50, verbose_name='No.')),
                ('department_name', models.CharField(max_length=50, verbose_name='Department Name')),
                ('performance_start_date', models.DateField(auto_now=True, verbose_name='Performance Start Date')),
                ('performance_end_date', models.DateField(auto_now=True, verbose_name='Performance End Date')),
                ('job_title', models.CharField(max_length=50, verbose_name='Job Title')),
                ('employment_date', models.DateField(auto_now=True, verbose_name='Employment Date')),
                ('supervisor_level', models.CharField(max_length=150, verbose_name='Supervisor Level')),
                ('supervisor_name', models.CharField(max_length=150, verbose_name='Supervisor Name')),
                ('supervisor_job_title', models.CharField(max_length=50, verbose_name='Supervisor Job Title')),
                ('next_supervisor_level', models.CharField(max_length=150, verbose_name='Supervisor Level')),
                ('next_supervisor_name', models.CharField(max_length=150, verbose_name='Next Supervisor Name')),
                ('next_supervisor_job_title', models.CharField(max_length=50, verbose_name='Next Supervisor Job Title')),
                ('employee_signed', models.BooleanField(verbose_name='Employee Signed')),
                ('employee_signed_date', models.DateField(auto_now=True, verbose_name='Employee Signed Date')),
                ('supervisor_signed', models.BooleanField(verbose_name='Supervisor Signed')),
                ('supervisor_signed_date', models.DateField(auto_now=True, verbose_name='Supervisor Signed Date')),
                ('next_supervisor_signed', models.BooleanField(verbose_name='Next Supervisor Signed')),
                ('next_supervisor_signed_date', models.DateField(auto_now=True, verbose_name='Next Supervisor Signed Date')),
                ('transation_date', models.DateField(auto_now=True, verbose_name='Transaction Date')),
                ('user_id', models.CharField(max_length=50, verbose_name='User ID')),
                ('no_series', models.CharField(max_length=50, verbose_name='No. Series')),
                ('posted', models.BooleanField(verbose_name='Posted')),
                ('final_review_complete', models.BooleanField(verbose_name='Final Review Complete')),
                ('total_individual_weights', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Total Individual Weights')),
                ('department_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.department', verbose_name='Department Code')),
                ('emp_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee', verbose_name='Employee Code')),
            ],
            options={
                'verbose_name': 'Individual Objective Setting',
                'verbose_name_plural': 'Individual Objective Settings',
            },
        ),
        migrations.CreateModel(
            name='IndividualObjectiveReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=50, verbose_name='No.')),
                ('department_name', models.CharField(max_length=50, verbose_name='Department Name')),
                ('performance_start_date', models.DateField(auto_now=True, verbose_name='Performance Start Date')),
                ('performance_end_date', models.DateField(auto_now=True, verbose_name='Performance End Date')),
                ('job_title', models.CharField(max_length=50, verbose_name='Job Title')),
                ('employment_date', models.DateField(auto_now=True, verbose_name='Employment Date')),
                ('supervisor_level', models.CharField(max_length=150, verbose_name='Supervisor Level')),
                ('supervisor_name', models.CharField(max_length=150, verbose_name='Supervisor Name')),
                ('supervisor_job_title', models.CharField(max_length=50, verbose_name='Supervisor Job Title')),
                ('next_supervisor_level', models.CharField(max_length=150, verbose_name='Supervisor Level')),
                ('next_supervisor_name', models.CharField(max_length=150, verbose_name='Next Supervisor Name')),
                ('next_supervisor_job_title', models.CharField(max_length=50, verbose_name='Next Supervisor Job Title')),
                ('employee_signed', models.BooleanField(verbose_name='Employee Signed')),
                ('employee_signed_date', models.DateField(auto_now=True, verbose_name='Employee Signed Date')),
                ('supervisor_signed', models.BooleanField(verbose_name='Supervisor Signed')),
                ('supervisor_signed_date', models.DateField(auto_now=True, verbose_name='Supervisor Signed Date')),
                ('next_supervisor_signed', models.BooleanField(verbose_name='Next Supervisor Signed')),
                ('next_supervisor_signed_date', models.DateField(auto_now=True, verbose_name='Next Supervisor Signed Date')),
                ('transation_date', models.DateField(auto_now=True, verbose_name='Transaction Date')),
                ('user_id', models.CharField(max_length=50, verbose_name='User ID')),
                ('no_series', models.CharField(max_length=50, verbose_name='No. Series')),
                ('emp_name', models.CharField(max_length=150, verbose_name='Employee Name')),
                ('department_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.department', verbose_name='Department Code')),
                ('emp_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee', verbose_name='Employee Code')),
                ('objective_setting_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objectivesapplication.individualobjectivesetting', verbose_name='Objective Setting Number')),
            ],
            options={
                'verbose_name': 'Individual Objective Review',
                'verbose_name_plural': 'Individual Objective Reviews',
            },
        ),
        migrations.CreateModel(
            name='IndividualObjectiveLines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_no', models.CharField(max_length=50, verbose_name='Header No.')),
                ('entry_no', models.PositiveIntegerField(verbose_name='Entry No.')),
                ('performance_target', models.CharField(max_length=250, verbose_name='Performance Target')),
                ('dept_objective_entry_no', models.PositiveIntegerField(verbose_name='Departmental Objective Entry No,')),
                ('measurement_indicator', models.CharField(max_length=50, verbose_name='Measurement Indicator')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Weight')),
                ('target_date', models.DateField(auto_now=True, verbose_name='Target Date')),
                ('corporate_objective_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objectivesapplication.cooperateobjectives', verbose_name='Corporate Objective Code')),
                ('dept_object_text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objectivesapplication.departmentalobjectives', verbose_name='Departmental Objective Text')),
            ],
            options={
                'verbose_name': 'Individual Objective Lines',
                'verbose_name_plural': 'Individual Objective Lines',
            },
        ),
    ]
