from typing import Any
from django.core.management.base import BaseCommand
from paygroup.models import PayGroup
from pprint import pprint
import requests
from environs import Env

env = Env()
env.read_env()

from requests_ntlm import HttpNtlmAuth
from company.models import Company

class Command(BaseCommand):
    help = "load data to database"

    def handle(self, *args: Any, **options: Any):
        self.stdout.write(self.style.SUCCESS("load data to database"))
        auth = HttpNtlmAuth(username=env.str("username"),password=env.str("password"))
        companies = Company.objects.all()
        
        for comp  in companies:
            if comp.name == "Rock City Hotel":
                self.stdout.write(self.style.SUCCESS(f"Starting load data to database {comp.id}"))           
                load_paygroup(url=env.str("rchpay_group"), auth=auth, company=comp.name, company_id=comp.id)
                self.stdout.write(self.style.SUCCESS("Successfully load data to database"))           


def load_paygroup(url, auth, company, company_id):
    res = requests.get(url=url, auth=auth)
    data = res.json()
    for paygroup in data["value"]:
        try:
            if PayGroup.objects.filter(no=paygroup["No"]).exists():
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
                    company=company,
                    company_id=company_id
                    )
            elif not PayGroup.objects.filter(no=paygroup["No"]).exists():
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
                    company_id=company_id,
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
                company=company,
                company_id = company_id
                )