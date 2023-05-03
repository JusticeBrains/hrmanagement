from typing import Any, Optional
from django.core.management.base import BaseCommand
from company.models import SalaryGrade, JobTitles
from employee.models import Department, Branch, Notch, PayCategoryList, Unit
import json
from pprint import pprint

class Command(BaseCommand):
    help = "load data to database"

    def handle(self, *args: Any, **options: Any):
        with open("employee/dep.json", 'r') as file:
            dep = json.load(file)
        
        with open("employee/branch.json", 'r') as file:
            branch = json.load(file)
        

        with open("employee/unit.json", 'r') as file:
            unit = json.load(file)

        with open("employee/jobtitles.json", 'r') as file:
            jobtitles = json.load(file)

        with open("employee/salarylevel.json", 'r') as file:
            salarylevel = json.load(file)

        with open("employee/notches.json", 'r') as file:
            notches = json.load(file)

        with open("employee/paycat.json", 'r') as file:
            paycat = json.load(file)

        print(f"--Loading Departments --")
        for val in dep["value"]:
            print(f"--Startng--{val['Code']} ")
            if not Department.objects.filter(code=val['Code']):
                Department.objects.create(
                    code=val["Code"],
                    name=val["Name"],
                    first_category_code=val["First_Category_Code"]
                )
            print(f"--End-- {val['Name']}")
        print(f"Done -- Departmen -- {Department.objects.all().count()}")


        print(f"--Loading Branch --")
        for val in branch["value"]:
            print(f"--Startng--{val['Code']} ")
            if not Branch.objects.filter(code=val['Code']):
                Branch.objects.create(
                    code=val["Code"],
                    name=val["Name"],
                    third_category_code=val["Third_Category_Code"]
                )
            print(f"--End-- {val['Name']}")
        print(f"Done -- Branch -- {Branch.objects.all().count()}")


        print(f"--Loading Units --")
        for val in unit["value"]:
            print(f"--Startng--{val['Code']} ")
            if not Unit.objects.filter(code=val['Code']):
                Unit.objects.create(
                    code=val["Code"],
                    name=val["Name"],
                    second_category_code=val["Second_Category_Code"]
                )
            print(f"--End-- {val['Name']}")
        print(f"Done -- Unit -- {Unit.objects.all().count()}")


        print(f"--Loading JobTitles --")
        for val in jobtitles["value"]:
            print(f"--Startng--{val['Code']} ")
            if not JobTitles.objects.filter(code=val['Code']):
                JobTitles.objects.create(
                    code=val["Code"],
                    # payroll_structure=val["Payroll_Structure"],
                    # salary_grade=val["Salary_Grade"],
                    description=val['Description']
                )
            print(f"--End-- {val['Description']}")
        print(f"Done -- Unit -- {JobTitles.objects.all().count()}")


        print(f"--Loading SalaryGrade --")
        for val in salarylevel["value"]:
            print(f"--Startng--{val['Code']} ")
            if not SalaryGrade.objects.filter(code=val['Code']):
                SalaryGrade.objects.create(
                    code=val["Code"],
                    payroll_structure=val["Payroll_Structure_Code"],
                    job_titles=val["Job_Titles"],
                    transport_rate=val['Transport_Rate']
                )
            print(f"--End-- {val['Code']}")
        print(f"Done -- Unit -- {SalaryGrade.objects.all().count()}")


        print(f"--Loading SalaryGrade --")
        for val in notches["value"]:
            print(f"--Startng--{val['Payroll_Structure_Code']} ")
            if not Notch.objects.filter(no=val['No'],payroll_structure_code=val["Payroll_Structure_Code"],salary_grade=val['Salary_Grade']):
                Notch.objects.create(
                    no=val['No'],
                    payroll_structure_code=val["Payroll_Structure_Code"],
                    amount=val["Amount"],
                    salary_grade=val['Salary_Grade']
                )
            print(f"--End-- {val['Payroll_Structure_Code']}")
        print(f"Done -- Notch -- {Notch.objects.all().count()}")


        print(f"--Loading SalaryGrade --")
        for val in paycat["value"]:
            print(f"--Startng--{val['Description']} ")
            if not PayCategoryList.objects.filter(no=val['No'], ):
                PayCategoryList.objects.create(
                    no=val['No'],
                    description=val["Description"],
                    taxable_income_code=val["Taxable_Income_Code"],
                    taxable_income_description=val['Taxable_Income_Description'],
                    tax_code=val['Tax_Code'],
                    gross_income_code=val['Tax_Description'],
                    gross_income_description=val['Gross_Income_Code'],
                    bonus_tax_code=val['Gross_Income_Description'],
                    bonus_tax_description=val['Bonus_Tax_Code'],
                    currency_code=val['Currency_Code'],
                )
            print(f"--End-- {val['Description']}")
        print(f"Done -- PayCategory -- {PayCategoryList.objects.all().count()}")