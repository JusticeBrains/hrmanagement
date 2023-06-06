from typing import Any, Optional
from django.core.management.base import BaseCommand
from company.models import SalaryGrade, JobTitles, Company
from employee.models import Department, Branch, Notch, PayGroup, Unit, Employee, StaffCategory
import json

import requests
from requests_ntlm import HttpNtlmAuth

from environs import Env

env = Env()
env.read_env()

class Command(BaseCommand):
    help = "load data to database"

    def handle(self, *args: Any, **options: Any):
        
        companies = Company.objects.all()

        auth = HttpNtlmAuth(username=env.str("username"),password=env.str("password"))

        load_department()

        for comp  in companies:
            if comp.name == "Rock City Hotel":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.id}"))           
                load_paygroup(url=env.str("rchpay_group"), auth=auth, company=comp.name)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
            if comp.name =="BRYAN ACHEAMPONG FOUNDATION":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.id} -- {comp.name}"))
                load_paygroup(url=env.str("baf_pay_group"), auth=auth, company=comp.name)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
            if comp.name =="Emery Invest":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.id} -- {comp.name}"))
                load_paygroup(url=env.str("emery_pay_group"), auth=auth, company=comp.name)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
            if comp.name =="CRONUS International Ltd.":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.id} -- {comp.name}"))
                load_paygroup(url=env.str("cronus_pay_group"), auth=auth, company=comp.name)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
            if comp.name =="FAAB Systems Gh. Ltd":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.id} -- {comp.name}"))
                load_paygroup(url=env.str("faab_pay_group"), auth=auth, company=comp.name)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
            if comp.name =="Rock City Hotel Heads of Department":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.id} -- {comp.name}"))
                load_paygroup(url=env.str("rock_hod_pay_group"), auth=auth, company=comp.name)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
            if comp.name =="INTERCITY STC COACHES LTD - JUNIOR STAFF":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.id} -- {comp.name}"))
                load_paygroup(url=env.str("intercity_jun_pay_group"), auth=auth, company=comp.name)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
            if comp.name =="INTERCITY STC COACHES LTD - DRIVERS":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.id} -- {comp.name}"))
                load_paygroup(url=env.str("intercity_driver_pay_group"), auth=auth, company=comp.name)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
            if comp.name =="INTERCITY STC COACHES LTD - SENIOR STAFF":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.id} -- {comp.name}"))
                load_paygroup(url=env.str("intercity_sen_pay_group"), auth=auth, company=comp.name)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
            if comp.name =="Intu IT Professional Allowance":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.id} -- {comp.name}"))
                load_paygroup(url=env.str("intuprof_allow_pay"), auth=auth, company=comp.name)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
            if comp.name =="NLA":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.id} -- {comp.name}"))
                # load_paygroup(url=env.str("nlajun_sen_paygroup"), auth=auth, company=comp.name)
                # self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
                
                load_paygroup(url=env.str("nla_exc_man_paygroup"), auth=auth, company=comp.name)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
                
                # load_paygroup(url=env.str("nla_man_paygroup"), auth=auth, company=comp.name)
                # self.stdout.write(self.style.SUCCESS("Successfully load data to database"))

            # if comp.name =="NLA EXECUTIVE MANAGEMENT":
            #     self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.id} -- {comp.name}"))
            #     load_paygroup(url=env.str("nla_exc_man_paygroup"), auth=auth, company=comp.name)
            #     self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
            # if comp.name =="NLA MANAGEMENT":
            #     self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.id} -- {comp.name}"))
            #     load_paygroup(url=env.str("nla_man_paygroup"), auth=auth, company=comp.name)
            #     self.stdout.write(self.style.SUCCESS("Successfully load data to database"))



        for company in companies:
            if company.name == "Emery Invest":
                get_user_data(url=env.str("emery"), auth=auth, company=company.name, company_id=company.id)
            elif company.name == "BRYAN ACHEAMPONG FOUNDATION":
                get_user_data(url=env.str("baf"), auth=auth, company=company.name, company_id=company.id)
            elif company.name == "FAAB Systems Gh. Ltd":
                get_user_data(url=env.str("faab"), auth=auth, company=company.name, company_id=company.id)
            elif company.name == "Rock City Hotel Heads of Department":
                get_user_data(url=env.str("rch_hod"), auth=auth, company=company.name, company_id=company.id)
            elif company.name == "REISS & CO. GHANA LIMITED":
                get_user_data(url=env.str("reiss_co"), auth=auth, company=company.name, company_id=company.id)
            elif company.name == "INTERCITY STC COACHES LTD - JUNIOR STAFF":
                get_user_data(url=env.str("intercity_jun"), auth=auth, company=company.name, company_id=company.id)
            elif company.name == "INTERCITY STC COACHES LTD - SENIOR STAFF":
                get_user_data(url=env.str("intercity_sen"), auth=auth, company=company.name, company_id=company.id)
            elif company.name == "INTERCITY STC COACHES LTD - DRIVERS":
                get_user_data(url=env.str("intercity_driver"), auth=auth, company=company.name, company_id=company.id)
            elif company.name == "M&B LIMITED":
                get_user_data(url=env.str("mb"), auth=auth, company=company.name, company_id=company.id)
            elif company.name == "Jays Lodge":
                get_user_data(url=env.str("jay_lodge"), auth=auth, company=company.name, company_id=company.id)
            elif company.name == "INTU-IT GHANA LIMITED":
                get_user_data(url=env.str("itu"), auth=auth, company=company.name, company_id=company.id)
            elif company.name == "Intu IT Professional Allowance":
                get_user_data(url=env.str("itu_allowance"), auth=auth, company=company.name, company_id=company.id)
            elif company.name == "Rock City Hotel Kumasi":
                get_user_data(url=env.str("rch_kumasi"), auth=auth, company=company.name, company_id=company.id)
            elif company.name == "Rock City Professional Allowance":
                get_user_data(url=env.str("rch_prof_allowance"), auth=auth, company=company.name, company_id=company.id)  
            elif company.name == "Rock City Hotel":
                get_user_data(url=env.str("rch"), auth=auth, company=company.name, company_id=company.id)
            elif company.name == "Republic Media Limited":
                get_user_data(url=env.str("rml"), auth=auth, company=company.name, company_id=company.id)
            elif company.name == "CRONUS International Ltd.":
                get_user_data(url=env.str("cronus"), auth=auth, company=company.name, company_id=company.id)
            elif company.name == "NLA":
                print("----Starting Management")
                get_user_data(url=env.str("nla_man"), auth=auth, company=company.name, company_id=company.id)
                print("----Ending Management---")
                print("----Starting Exec Management--")
                get_user_data(url=env.str("nla_exc_man"), auth=auth, company=company.name, company_id=company.id)
                print("----Starting Jun Senior")
                get_user_data(url=env.str("nlajun_sen"), auth=auth, company=company.name, company_id=company.id)

            # elif company.name == "NLA EXECUTIVE MANAGEMENT":
            #     get_user_data(url=env.str("nla_exc_man"), auth=auth, company=company.name, company_id=company.id)
            # elif company.name == "NLA JUNIOR AND SENIOR":
            #     get_user_data(url=env.str("nlajun_sen"), auth=auth, company=company.name, company_id=company.id)



def get_user_data(url, auth, company, company_id):
        res = requests.get(url=url, auth=auth)
        data = res.json()

        for employee in data['value']:
            if employee["Status"] == 'Active':
                print(f"{employee['No'] }- {employee['Status']}")
                try:
                    
                    if Employee.objects.filter(code=employee['No']).exists():
                        employee_obj = Employee.objects.get(code=employee['No'])
                        print(f"--updating-- {employee_obj}")
                        Employee.objects.filter(id=employee_obj.id).update(
                        code=employee['No'],
                        first_name=employee["First_Name"],
                        middle_name=employee["Middle_Name"],
                        last_name=employee["Last_Name"],
                        gender=employee["Gender"],
                        phone_no2=employee["Phone_No_2"],
                        company_email=employee["Company_E_Mail"],
                        job_titles=employee["Job_Titles"],
                        job_title_description=employee["Job_Title_Description"],
                        privacy_blocked=employee["Privacy_Blocked"],
                        address=employee["Address"],
                        address_2=employee["Address_2"],
                        post_code=employee["Post_Code"],
                        city=employee["City"],
                        country_region_code=employee["Country_Region_Code"],
                        showmap=employee["ShowMap"],
                        mobile_no=employee["Mobile_Phone_No"],
                        pager=employee["Pager"],
                        extension=employee["Extension"],
                        email=employee["E_Mail"],
                        alt_address_code=employee["Alt_Address_Code"],
                        alt_address_start_date=employee["Alt_Address_Start_Date"],
                        alt_address_end_date=employee["Alt_Address_End_Date"],
                        first_category_level=employee["First_Category_Level"],
                        second_category_level=employee["Second_Category_Level"],
                        third_category_level=employee["Third_Category_Level"],
                        fourth_category_level=employee["Fourth_Category_Level"],
                        fifth_category_level=employee["Fifth_Category_Level"],
                        employment_date=employee["Employment_Date"],
                        status=employee["Status"],
                        inactive_date=employee["Inactive_Date"],
                        cause_of_inactivity_code=employee["Cause_of_Inactivity_Code"],
                        termination_date=employee["Termination_Date"],
                        employement_contract_code=employee["Emplymt_Contract_Code"],
                        resource_no=employee["Resource_No"],
                        salesperson_purch_code=employee["Salespers_Purch_Code"],
                        birth_date=employee["Birth_Date"],
                        ssno=employee["Social_Security_No"],
                        union_code=employee["Union_Code"],
                        union_membership_number=["Union_Membership_No"],
                        employee_posting_group=employee["Employee_Posting_Group"],
                        application_method=employee["Application_Method"],
                        pay_group_code=employee["Pay_Group_Code"],
                        salary_grade=employee["Salary_Grade_Code"],
                        notch=employee["Notch"],
                        annual_basic=employee["Annual_Basic"],
                        contribute_to_ssf_employee=employee["Contribute_to_SSF_Employee"],
                        contribute_to_ssf_employer=employee["Contribute_to_SSF_Employer"],
                        payment_mode=employee["Payment_Mode"],
                        payment_method=employee["Payment_Method"],
                        bank_code=employee["Bank_Code"],
                        bank_name=employee["Bank_Name"],
                        bank_branch_code=employee["Branch_Code"],
                        bank_branch_name=employee["Branch_Name"],
                        bank_account_no=employee["Account_No"],
                        currency=employee["Currency"],
                        iban=employee["IBAN"],
                        swift_code=employee["SWIFT_Code"],
                        grounds_for_term=employee["Grounds_for_Term_Code"],
                        company=company, 
                        company_id=company_id
                )
                    if not Employee.objects.filter(code=employee['No']).exists():
                        print(f"--creating-- {employee['No']}")
                        Employee.objects.create(
                        code=employee['No'],
                        first_name=employee["First_Name"],
                        middle_name=employee["Middle_Name"],
                        last_name=employee["Last_Name"],
                        gender=employee["Gender"],
                        phone_no2=employee["Phone_No_2"],
                        company_email=employee["Company_E_Mail"],
                        job_titles=employee["Job_Titles"],
                        job_title_description=employee["Job_Title_Description"],
                        privacy_blocked=employee["Privacy_Blocked"],
                        address=employee["Address"],
                        address_2=employee["Address_2"],
                        post_code=employee["Post_Code"],
                        city=employee["City"],
                        country_region_code=employee["Country_Region_Code"],
                        showmap=employee["ShowMap"],
                        mobile_no=employee["Mobile_Phone_No"],
                        pager=employee["Pager"],
                        extension=employee["Extension"],
                        email=employee["E_Mail"],
                        alt_address_code=employee["Alt_Address_Code"],
                        alt_address_start_date=employee["Alt_Address_Start_Date"],
                        alt_address_end_date=employee["Alt_Address_End_Date"],
                        first_category_level=employee["First_Category_Level"],
                        second_category_level=employee["Second_Category_Level"],
                        third_category_level=employee["Third_Category_Level"],
                        fourth_category_level=employee["Fourth_Category_Level"],
                        fifth_category_level=employee["Fifth_Category_Level"],
                        employment_date=employee["Employment_Date"],
                        status=employee["Status"],
                        inactive_date=employee["Inactive_Date"],
                        cause_of_inactivity_code=employee["Cause_of_Inactivity_Code"],
                        termination_date=employee["Termination_Date"],
                        employement_contract_code=employee["Emplymt_Contract_Code"],
                        resource_no=employee["Resource_No"],
                        salesperson_purch_code=employee["Salespers_Purch_Code"],
                        birth_date=employee["Birth_Date"],
                        ssno=employee["Social_Security_No"],
                        union_code=employee["Union_Code"],
                        union_membership_number=["Union_Membership_No"],
                        employee_posting_group=employee["Employee_Posting_Group"],
                        application_method=employee["Application_Method"],
                        pay_group_code=employee["Pay_Group_Code"],
                        salary_grade=employee["Salary_Grade_Code"],
                        notch=employee["Notch"],
                        annual_basic=employee["Annual_Basic"],
                        contribute_to_ssf_employee=employee["Contribute_to_SSF_Employee"],
                        contribute_to_ssf_employer=employee["Contribute_to_SSF_Employer"],
                        payment_mode=employee["Payment_Mode"],
                        payment_method=employee["Payment_Method"],
                        bank_code=employee["Bank_Code"],
                        bank_name=employee["Bank_Name"],
                        bank_branch_code=employee["Branch_Code"],
                        bank_branch_name=employee["Branch_Name"],
                        bank_account_no=employee["Account_No"],
                        currency=employee["Currency"],
                        iban=employee["IBAN"],
                        swift_code=employee["SWIFT_Code"],
                        grounds_for_term=employee["Grounds_for_Term_Code"],
                        # days_left = staff_category.max_number_of_days,
                        company = company,
                        company_id=company_id

                )
                    print(f"Ending -- Employee {employee['No']}")
                except Employee.DoesNotExist:
                    # elif not Employee.objects.filter(code=employee['No']).exists:
                    print(f"--creating-- {employee['No']}")
                    Employee.objects.create(
                    code=employee['No'],
                    first_name=employee["First_Name"],
                    middle_name=employee["Middle_Name"],
                    last_name=employee["Last_Name"],
                    gender=employee["Gender"],
                    phone_no2=employee["Phone_No_2"],
                    company_email=employee["Company_E_Mail"],
                    job_titles=employee["Job_Titles"],
                    job_title_description=employee["Job_Title_Description"],
                    privacy_blocked=employee["Privacy_Blocked"],
                    address=employee["Address"],
                    address_2=employee["Address_2"],
                    post_code=employee["Post_Code"],
                    city=employee["City"],
                    country_region_code=employee["Country_Region_Code"],
                    showmap=employee["ShowMap"],
                    mobile_no=employee["Mobile_Phone_No"],
                    pager=employee["Pager"],
                    extension=employee["Extension"],
                    email=employee["E_Mail"],
                    alt_address_code=employee["Alt_Address_Code"],
                    alt_address_start_date=employee["Alt_Address_Start_Date"],
                    alt_address_end_date=employee["Alt_Address_End_Date"],
                    first_category_level=employee["First_Category_Level"],
                    second_category_level=employee["Second_Category_Level"],
                    third_category_level=employee["Third_Category_Level"],
                    fourth_category_level=employee["Fourth_Category_Level"],
                    fifth_category_level=employee["Fifth_Category_Level"],
                    employment_date=employee["Employment_Date"],
                    status=employee["Status"],
                    inactive_date=employee["Inactive_Date"],
                    cause_of_inactivity_code=employee["Cause_of_Inactivity_Code"],
                    termination_date=employee["Termination_Date"],
                    employement_contract_code=employee["Emplymt_Contract_Code"],
                    resource_no=employee["Resource_No"],
                    salesperson_purch_code=employee["Salespers_Purch_Code"],
                    birth_date=employee["Birth_Date"],
                    ssno=employee["Social_Security_No"],
                    union_code=employee["Union_Code"],
                    union_membership_number=["Union_Membership_No"],
                    employee_posting_group=employee["Employee_Posting_Group"],
                    application_method=employee["Application_Method"],
                    pay_group_code=employee["Pay_Group_Code"],
                    salary_grade=employee["Salary_Grade_Code"],
                    notch=employee["Notch"],
                    annual_basic=employee["Annual_Basic"],
                    contribute_to_ssf_employee=employee["Contribute_to_SSF_Employee"],
                    contribute_to_ssf_employer=employee["Contribute_to_SSF_Employer"],
                    payment_mode=employee["Payment_Mode"],
                    payment_method=employee["Payment_Method"],
                    bank_code=employee["Bank_Code"],
                    bank_name=employee["Bank_Name"],
                    bank_branch_code=employee["Branch_Code"],
                    bank_branch_name=employee["Branch_Name"],
                    bank_account_no=employee["Account_No"],
                    currency=employee["Currency"],
                    iban=employee["IBAN"],
                    swift_code=employee["SWIFT_Code"],
                    grounds_for_term=employee["Grounds_for_Term_Code"],
                    # days_left = staff_category.max_number_of_days,
                    company = company, 
                    company_id=company_id

                )
                    print(f"Ending -- Employee {employee['No']}")



def load_paygroup(url, auth, company):
    res = requests.get(url=url, auth=auth)
    data = res.json()
    for paygroup in data["value"]:
        try:
            if PayGroup.objects.filter(no=paygroup["No"], company=company).exists():
                paygroup_id = PayGroup.objects.get(no=paygroup['No'])
                print("Updating Existing Paygroup")
                PayGroup.objects.filter(no=paygroup_id).update(
                    no=paygroup["No"],
                    description=paygroup["Description"],
                    taxable_income_code=paygroup["Taxable_Income_Code"],
                    taxable_income_description=paygroup["Taxable_Income_Description"],
                    tax_code=paygroup["Tax_Code"],
                    tax_description=paygroup["Tax_Description"],
                    gross_income_code=paygroup["Gross_Income_Code"],
                    gross_income_description=paygroup["Gross_Income_Description"],
                    currency_code=paygroup["Currency_Code"],
                    bonus_tax_code=paygroup["Bonus_Tax_Code"],
                    bonus_tax_description=paygroup["Bonus_Tax_Description"],
                    gross_up=paygroup["Gross_Up"],
                    company=company
                    )
            elif not PayGroup.objects.filter(no=paygroup["No"], company=company).exists():
                print("Creating Paygroup")
                PayGroup.objects.create(
                    no=paygroup["No"],
                    description=paygroup["Description"],
                    taxable_income_code=paygroup["Taxable_Income_Code"],
                    taxable_income_description=paygroup["Taxable_Income_Description"],
                    tax_code=paygroup["Tax_Code"],
                    tax_description=paygroup["Tax_Description"],
                    gross_income_code=paygroup["Gross_Income_Code"],
                    gross_income_description=paygroup["Gross_Income_Description"],
                    currency_code=paygroup["Currency_Code"],
                    bonus_tax_code=paygroup["Bonus_Tax_Code"],
                    bonus_tax_description=paygroup["Bonus_Tax_Description"],
                    gross_up=paygroup["Gross_Up"],
                    company=company
                    )
        except PayGroup.DoesNotExist:
            print("Creating Paygroup If Paygroup doesnot exist")
            PayGroup.objects.create(
                no=paygroup["No"],
                description=paygroup["Description"],
                taxable_income_code=paygroup["Taxable_Income_Code"],
                taxable_income_description=paygroup["Taxable_Income_Description"],
                tax_code=paygroup["Tax_Code"],
                tax_description=paygroup["Tax_Description"],
                gross_income_code=paygroup["Gross_Income_Code"],
                gross_income_description=paygroup["Gross_Income_Description"],
                currency_code=paygroup["Currency_Code"],
                bonus_tax_code=paygroup["Bonus_Tax_Code"],
                bonus_tax_description=paygroup["Bonus_Tax_Description"],
                gross_up=paygroup["Gross_Up"],
                company=company
                )


def load_department():
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

