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

        self.stdout.write(self.style.SUCCESS(f"--------Loading Departments-------"))
        for comp in companies:
            if comp.name == "INTERCITY STC COACHES LTD - SENIOR STAFF":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.name}"))           
                load_department(url=env.str("intercity_sen_dep"), auth=auth, company=comp.name, comp_id=comp.id)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))

            if comp.name == "INTERCITY STC COACHES LTD - JUNIOR STAFF":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.name}"))           
                load_department(url=env.str("intercity_jun_dep"), auth=auth, company=comp.name, comp_id=comp.id)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
        
            if comp.name == "Rock City Hotel":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.name}"))           
                load_department(url=env.str("rch_dep"), auth=auth, company=comp.name, comp_id=comp.id)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
  
            if comp.name == "BRYAN ACHEAMPONG FOUNDATION":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.name}"))           
                load_department(url=env.str("baf_dep"), auth=auth, company=comp.name, comp_id=comp.id)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
  
            if comp.name == "Emery Invest":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.name}"))           
                load_department(url=env.str("emery_dep"), auth=auth, company=comp.name, comp_id=comp.id)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
  
            if comp.name == "CRONUS International Ltd.":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.name}"))           
                load_department(url=env.str("cronus_dep"), auth=auth, company=comp.name, comp_id=comp.id)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))

            if comp.name == "FAAB Systems Gh. Ltd":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.name}"))           
                load_department(url=env.str("faab_dep"), auth=auth, company=comp.name, comp_id=comp.id)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))


            if comp.name == "Rock City Hotel Heads of Department":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.id}"))           
                load_department(url=env.str("rch_hod_dep"), auth=auth, company=comp.name, comp_id=comp.id)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))


            if comp.name == "Republic Media Limited":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.id}"))           
                load_department(url=env.str("repub_dep"), auth=auth, company=comp.name, comp_id=comp.id)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))

            if comp.name == "INTERCITY STC COACHES LTD - DRIVERS":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.id}"))           
                load_department(url=env.str("intercity_driver_dep"), auth=auth, company=comp.name, comp_id=comp.id)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))

            if comp.name == "Intu IT Professional Allowance":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.id}"))           
                load_department(url=env.str("intuprof_dep"), auth=auth, company=comp.name, comp_id=comp.id)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
 
            if comp.name == "INTU-IT GHANA LIMITED":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.id}"))           
                load_department(url=env.str("inut_dep"), auth=auth, company=comp.name, comp_id=comp.id)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
 
            if comp.name == "Rock City Professional Allowance":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.id}"))           
                load_department(url=env.str("rch_prof_allowance_dep"), auth=auth, company=comp.name, comp_id=comp.id)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))

        self.stdout.write(self.style.SUCCESS(f"-------- Done Loading Departments-------"))


        self.stdout.write(self.style.SUCCESS(f"--------Loading PayGroups-------"))

        for comp  in companies:
            if comp.name == "Rock City Hotel":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.id}"))           
                load_paygroup(url=env.str("rchpay_group"), auth=auth, company=comp.name, comp_id=comp.id)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
            if comp.name =="BRYAN ACHEAMPONG FOUNDATION":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.id} -- {comp.name}"))
                load_paygroup(url=env.str("baf_pay_group"), auth=auth, company=comp.name, comp_id=comp.id)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
            if comp.name =="Emery Invest":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.id} -- {comp.name}"))
                load_paygroup(url=env.str("emery_pay_group"), auth=auth, company=comp.name, comp_id=comp.id)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
            if comp.name =="CRONUS International Ltd.":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.id} -- {comp.name}"))
                load_paygroup(url=env.str("cronus_pay_group"), auth=auth, company=comp.name, comp_id=comp.id)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
            if comp.name =="FAAB Systems Gh. Ltd":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.id} -- {comp.name}"))
                load_paygroup(url=env.str("faab_pay_group"), auth=auth, company=comp.name, comp_id=comp.id)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
            if comp.name =="Rock City Hotel Heads of Department":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.id} -- {comp.name}"))
                load_paygroup(url=env.str("rock_hod_pay_group"), auth=auth, company=comp.name, comp_id=comp.id)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
            if comp.name =="INTERCITY STC COACHES LTD - JUNIOR STAFF":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.id} -- {comp.name}"))
                load_paygroup(url=env.str("intercity_jun_pay_group"), auth=auth, company=comp.name, comp_id=comp.id)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
            if comp.name =="INTERCITY STC COACHES LTD - DRIVERS":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.id} -- {comp.name}"))
                load_paygroup(url=env.str("intercity_driver_pay_group"), auth=auth, company=comp.name, comp_id=comp.id)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
            if comp.name =="INTERCITY STC COACHES LTD - SENIOR STAFF":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.id} -- {comp.name}"))
                load_paygroup(url=env.str("intercity_sen_pay_group"), auth=auth, company=comp.name, comp_id=comp.id)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
            if comp.name =="Intu IT Professional Allowance":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.id} -- {comp.name}"))
                load_paygroup(url=env.str("intuprof_allow_pay"), auth=auth, company=comp.name, comp_id=comp.id)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
            if comp.name =="NLA":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.id} -- {comp.name}"))        
                load_paygroup(url=env.str("nla_exc_man_paygroup"), auth=auth, company=comp.name,comp_id=comp.id)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
            if comp.name == "Republic Media Limited":
                load_paygroup(url=env.str("repub_paygroup"), auth=auth, company=comp.name, comp_id=comp.id)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))

            if comp.name == "Rock City Professional Allowance":
                load_paygroup(url=env.str("nlajun_sen_paygroup"), auth=auth, company=comp.name, comp_id=comp.id)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
        
        self.stdout.write(self.style.SUCCESS(f"--------Ended Loading PayGroups-------"))
        

            # if comp.name =="NLA EXECUTIVE MANAGEMENT":
            #     self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.id} -- {comp.name}"))
            #     load_paygroup(url=env.str("nla_exc_man_paygroup"), auth=auth, company=comp.name)
            #     self.stdout.write(self.style.SUCCESS("Successfully load data to database"))
            # if comp.name =="NLA MANAGEMENT":
            #     self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.id} -- {comp.name}"))
            #     load_paygroup(url=env.str("nla_man_paygroup"), auth=auth, company=comp.name)
            #     self.stdout.write(self.style.SUCCESS("Successfully load data to database"))


        self.stdout.write(self.style.SUCCESS(f"--------Loading Employees-------"))

        for company in companies:
            # if company.name == "Emery Invest":
            #     self.stdout.write(self.style.SUCCESS(f"Starting load data to database {company.id} -- {company.name}"))        
            #     get_user_data(url=env.str("emery"), auth=auth, company=company.name, company_id=company.id)
            #     self.stdout.write(self.style.SUCCESS("Successfully load data to database"))

            # if company.name == "BRYAN ACHEAMPONG FOUNDATION":
            #     self.stdout.write(self.style.SUCCESS(f"Starting load data to database {company.id} -- {company.name}"))        
            #     get_user_data(url=env.str("baf"), auth=auth, company=company.name, company_id=company.id)
            #     self.stdout.write(self.style.SUCCESS("Successfully load data to database"))

            # if company.name == "FAAB Systems Gh. Ltd":
            #     self.stdout.write(self.style.SUCCESS(f"Starting load data to database {company.id} -- {company.name}"))        
            #     get_user_data(url=env.str("faab"), auth=auth, company=company.name, company_id=company.id)
            #     self.stdout.write(self.style.SUCCESS("Successfully load data to database"))

            # if company.name == "Rock City Hotel Heads of Department":
            #     self.stdout.write(self.style.SUCCESS(f"Starting load data to database {company.id} -- {company.name}"))        
            #     get_user_data(url=env.str("rch_hod"), auth=auth, company=company.name, company_id=company.id)
            #     self.stdout.write(self.style.SUCCESS("Successfully load data to database"))

            # if company.name == "REISS & CO. GHANA LIMITED":
            #     self.stdout.write(self.style.SUCCESS(f"Starting load data to database {company.id} -- {company.name}"))        
            #     get_user_data(url=env.str("reiss_co"), auth=auth, company=company.name, company_id=company.id)
            #     self.stdout.write(self.style.SUCCESS("Successfully load data to database"))

            # if company.name == "INTERCITY STC COACHES LTD - JUNIOR STAFF":
            #     self.stdout.write(self.style.SUCCESS(f"Starting load data to database {company.id} -- {company.name}"))        
            #     get_user_data(url=env.str("intercity_jun"), auth=auth, company=company.name, company_id=company.id)
            #     self.stdout.write(self.style.SUCCESS("Successfully load data to database"))

            # if company.name == "INTERCITY STC COACHES LTD - SENIOR STAFF":
            #     self.stdout.write(self.style.SUCCESS(f"Starting load data to database {company.id} -- {company.name}"))        
            #     get_user_data(url=env.str("intercity_sen"), auth=auth, company=company.name, company_id=company.id)
            #     self.stdout.write(self.style.SUCCESS("Successfully load data to database"))

            # if company.name == "INTERCITY STC COACHES LTD - DRIVERS":
            #     self.stdout.write(self.style.SUCCESS(f"Starting load data to database {company.id} -- {company.name}"))        
            #     get_user_data(url=env.str("intercity_driver"), auth=auth, company=company.name, company_id=company.id)
            #     self.stdout.write(self.style.SUCCESS("Successfully load data to database"))

            # if company.name == "M&B LIMITED":
            #     self.stdout.write(self.style.SUCCESS(f"Starting load data to database {company.id} -- {company.name}"))        
            #     get_user_data(url=env.str("mb"), auth=auth, company=company.name, company_id=company.id)
            #     self.stdout.write(self.style.SUCCESS("Successfully load data to database"))

            # if company.name == "Jays Lodge":
            #     self.stdout.write(self.style.SUCCESS(f"Starting load data to database {company.id} -- {company.name}"))        
            #     get_user_data(url=env.str("jay_lodge"), auth=auth, company=company.name, company_id=company.id)
            #     self.stdout.write(self.style.SUCCESS("Successfully load data to database"))

            # if company.name == "INTU-IT GHANA LIMITED":
            #     self.stdout.write(self.style.SUCCESS(f"Starting load data to database {company.id} -- {company.name}"))        
            #     get_user_data(url=env.str("itu"), auth=auth, company=company.name, company_id=company.id)
            #     self.stdout.write(self.style.SUCCESS("Successfully load data to database"))

            if company.name == "Intu IT Professional Allowance":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {company.id} -- {company.name}"))        
                get_user_data(url=env.str("itu_allowance"), auth=auth, company=company.name, company_id=company.id)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))

            # elif company.name == "Rock City Hotel Kumasi":
            #     self.stdout.write(self.style.SUCCESS(f"Starting load data to database {company.id} -- {company.name}"))        
            #     get_user_data(url=env.str("rch_kumasi"), auth=auth, company=company.name, company_id=company.id)
            #     self.stdout.write(self.style.SUCCESS("Successfully load data to database"))

            # elif company.name == "Rock City Professional Allowance":
            #     self.stdout.write(self.style.SUCCESS(f"Starting load data to database {company.id} -- {company.name}"))        
            #     get_user_data(url=env.str("rch_prof_allowance"), auth=auth, company=company.name, company_id=company.id)  
            #     self.stdout.write(self.style.SUCCESS("Successfully load data to database"))

            # elif company.name == "Rock City Hotel":
            #     self.stdout.write(self.style.SUCCESS(f"Starting load data to database {company.id} -- {company.name}"))        
            #     get_user_data(url=env.str("rch"), auth=auth, company=company.name, company_id=company.id)
            #     self.stdout.write(self.style.SUCCESS("Successfully load data to database"))

            # elif company.name == "Republic Media Limited":
            #     self.stdout.write(self.style.SUCCESS(f"Starting load data to database {company.id} -- {company.name}"))        
            #     get_user_data(url=env.str("rml"), auth=auth, company=company.name, company_id=company.id)
            #     self.stdout.write(self.style.SUCCESS("Successfully load data to database"))

            # if company.name == "CRONUS International Ltd.":
            #     self.stdout.write(self.style.SUCCESS(f"Starting load data to database {company.id} -- {company.name}"))        
            #     get_user_data(url=env.str("cronus"), auth=auth, company=company.name, company_id=company.id)
            #     self.stdout.write(self.style.SUCCESS("Successfully load data to database"))

            # if company.name == "NLA":
            #     self.stdout.write(self.style.SUCCESS(f"Starting load data to database {company.id} -- {company.name}"))        
            #     self.stdout.write(self.style.SUCCESS(f"----Starting Management"))
            #     get_user_data(url=env.str("nla_man"), auth=auth, company=company.name, company_id=company.id)
            #     self.stdout.write(self.style.SUCCESS(f"----Ending Management---"))
            #     self.stdout.write(self.style.SUCCESS(f"----Starting Exec Management--"))
            #     get_user_data(url=env.str("nla_exc_man"), auth=auth, company=company.name, company_id=company.id)
            #     self.stdout.write(self.style.SUCCESS(f"----Starting Jun Senior"))
            #     get_user_data(url=env.str("nlajun_sen"), auth=auth, company=company.name, company_id=company.id)
            #     self.stdout.write(self.style.SUCCESS("Successfully load data to database"))

        self.stdout.write(self.style.SUCCESS(f"--------Ended Loading Employees-------"))


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



def load_paygroup(url, auth, company, comp_id):
    res = requests.get(url=url, auth=auth)
    data = res.json()
    for paygroup in data["value"]:
        try:
            if PayGroup.objects.filter(no=paygroup["No"], company=company).exists():
                paygroup_id = PayGroup.objects.get(no=paygroup['No'],company=company)
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
                    company=company,
                    comp_id=comp_id
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
                    company=company,
                    comp_id=comp_id
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
                company=company,
                comp_id=comp_id
                )


def load_department(url, auth, company, comp_id):
    res = requests.get(url=url, auth=auth)
    data = res.json()
    for dep in data["value"]:
        if Department.objects.filter(code=dep["Code"], company=company).exists():
            dep_id = Department.objects.get(code=dep['Code'],company=company)
            print("Updating Existing Departments")
            Department.objects.filter(code=dep_id).update(
                code = dep["Code"],
                name = dep['Name'],
                first_category_code=dep["First_Category_Code"],
                company=company,
                company_id=comp_id
            )
        elif not Department.objects.filter(code=dep["Code"], company=company).exists():
            print("------Creating New Department------")
            Department.objects.create(
                code=dep["Code"],
                name=dep['Name'],
                first_category_code=dep["First_Category_Code"],
                company=company,
                company_id=comp_id
            )
      
