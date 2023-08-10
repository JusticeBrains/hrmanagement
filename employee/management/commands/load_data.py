from typing import Any
from django.core.management.base import BaseCommand
from company.models import JobTitles, Company
from employee.models import (
    Branch,
    Department,
    PayGroup,
    Employee,
    Unit,
)
import logging
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from asgiref.sync import sync_to_async
import requests
import asyncio
import aiohttp
from requests_ntlm import HttpNtlmAuth
from django.conf import settings
from environs import Env

env = Env()
env.read_env()

logging.basicConfig(level=logging.DEBUG)


class Command(BaseCommand):
    help = "load data to database"

    def handle(self, *args: Any, **options: Any):
        companies = Company.objects.all()

        auth = HttpNtlmAuth(username=env.str("username"), password=env.str("password"))

        self.stdout.write(self.style.SUCCESS("--------Loading Departments-------"))
        for comp in companies:
            if comp.name == "INTERCITY STC LTD":
                self.stdout.write(
                    self.style.SUCCESS(f"Starting load data to database {comp.name}")
                )
                asyncio.run(load_department(
                    url=env.str("intercity_sen_dep"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                ))

                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

                self.stdout.write(
                    self.style.SUCCESS(f"Starting load data to database {comp.name}")
                )
                asyncio.run(load_department(
                    url=env.str("intercity_jun_dep"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                ))
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

                self.stdout.write(
                    self.style.SUCCESS(f"Starting load data to database {comp.id}")
                )
                asyncio.run(load_department(
                    url=env.str("intercity_driver_dep"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                ))
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "Rock City Hotel":
                self.stdout.write(
                    self.style.SUCCESS(f"Starting load data to database {comp.name}")
                )
                asyncio.run(load_department(
                    url=env.str("rch_dep"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                ))
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "BRYAN ACHEAMPONG FOUNDATION":
                self.stdout.write(
                    self.style.SUCCESS(f"Starting load data to database {comp.name}")
                )
                asyncio.run(load_department(
                    url=env.str("baf_dep"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                ))
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "Emery Invest":
                self.stdout.write(
                    self.style.SUCCESS(f"Starting load data to database {comp.name}")
                )
                asyncio.run(load_department(
                    url=env.str("emery_dep"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                ))
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "FAAB Systems Gh. Ltd":
                self.stdout.write(
                    self.style.SUCCESS(f"Starting load data to database {comp.name}")
                )
                asyncio.run(load_department(
                    url=env.str("faab_dep"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                ))
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "Rock City Hotel Heads of Department":
                self.stdout.write(
                    self.style.SUCCESS(f"Starting load data to database {comp.id}")
                )
                asyncio.run(load_department(
                    url=env.str("rch_hod_dep"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                ))
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "Republic Media Limited":
                self.stdout.write(
                    self.style.SUCCESS(f"Starting load data to database {comp.id}")
                )
                asyncio.run(load_department(
                    url=env.str("repub_dep"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                ))
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "Intu IT Professional Allowance":
                self.stdout.write(
                    self.style.SUCCESS(f"Starting load data to database {comp.id}")
                )
                asyncio.run(load_department(
                    url=env.str("intuprof_dep"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                ))
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "INTU-IT GHANA LIMITED":
                self.stdout.write(
                    self.style.SUCCESS(f"Starting load data to database {comp.id}")
                )
                asyncio.run(load_department(
                    url=env.str("inut_dep"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                ))
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "Rock City Professional Allowance":
                self.stdout.write(
                    self.style.SUCCESS(f"Starting load data to database {comp.id}")
                )
                asyncio.run(load_department(
                    url=env.str("rch_prof_allowance_dep"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                ))
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )
            if comp.name == "NLA MANAGEMENT":
                self.stdout.write(
                    self.style.SUCCESS(f"Starting load data to database {comp.id}")
                )
                asyncio.run(load_department(
                    url=env.str("nla_exc_man_dep"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                ))
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )
            if comp.name == "NLA JUNIOR SENIOR":
                self.stdout.write(
                    self.style.SUCCESS(f"Starting load data to database {comp.id}")
                )
                asyncio.run(load_department(
                    url=env.str("nla_jun_sen_dep"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                ))
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )
        self.stdout.write(
            self.style.SUCCESS("-------- Done Loading Departments-------")
        )

        self.stdout.write(
            self.style.SUCCESS("--------Starting Loading JobTitles-------")
        )

        for comp in companies:
            if comp.name == "Rock City Hotel":
                self.stdout.write(
                    self.style.SUCCESS(f"Starting load data to database {comp.id}")
                )
                asyncio.run(
                    load_jobtitles(
                        url=env.str("rch_jobs"),
                        auth=auth,
                        company=comp.name,
                        comp_id=comp.id,
                    )
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "BRYAN ACHEAMPONG FOUNDATION":
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Starting load data to database {comp.id} -- {comp.name}"
                    )
                )
                asyncio.run(
                    load_jobtitles(
                        url=env.str("baf_jobs"),
                        auth=auth,
                        company=comp.name,
                        comp_id=comp.id,
                    )
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "Emery Invest":
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Starting load data to database {comp.id} -- {comp.name}"
                    )
                )
                asyncio.run(
                    load_jobtitles(
                        url=env.str("emery_jobs"),
                        auth=auth,
                        company=comp.name,
                        comp_id=comp.id,
                    )
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "FAAB Systems Gh. Ltd":
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Starting load data to database {comp.id} -- {comp.name}"
                    )
                )
                asyncio.run(
                    load_jobtitles(
                        url=env.str("faab_jobs"),
                        auth=auth,
                        company=comp.name,
                        comp_id=comp.id,
                    )
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )
            if comp.name == "Rock City Hotel Heads of Department":
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Starting load data to database {comp.id} -- {comp.name}"
                    )
                )
                asyncio.run(
                    load_jobtitles(
                        url=env.str("rch_hod_jobs"),
                        auth=auth,
                        company=comp.name,
                        comp_id=comp.id,
                    )
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "INTERCITY STC LTD":
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Starting load data to database {comp.id} -- {comp.name}"
                    )
                )
                asyncio.run(
                    load_jobtitles(
                        url=env.str("intercity_jun_jobs"),
                        auth=auth,
                        company=comp.name,
                        comp_id=comp.id,
                    )
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

                self.stdout.write(
                    self.style.SUCCESS(
                        f"Starting load data to database {comp.id} -- {comp.name}"
                    )
                )
                asyncio.run(
                    load_jobtitles(
                        url=env.str("intercity_driver_jobs"),
                        auth=auth,
                        company=comp.name,
                        comp_id=comp.id,
                    )
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

                self.stdout.write(
                    self.style.SUCCESS(
                        f"Starting load data to database {comp.id} -- {comp.name}"
                    )
                )
                asyncio.run(
                    load_jobtitles(
                        url=env.str("intercity_sen_jobs"),
                        auth=auth,
                        company=comp.name,
                        comp_id=comp.id,
                    )
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "Intu IT Professional Allowance":
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Starting load data to database {comp.id} -- {comp.name}"
                    )
                )
                asyncio.run(
                    load_jobtitles(
                        url=env.str("intuprof_jobs"),
                        auth=auth,
                        company=comp.name,
                        comp_id=comp.id,
                    )
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )
            if comp.name == "NLA MANAGEMENT":
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Starting load data to database {comp.id} -- {comp.name}"
                    )
                )
                asyncio.run(
                    load_jobtitles(
                        url=env.str("nla_man_jobs"),
                        auth=auth,
                        company=comp.name,
                        comp_id=comp.id,
                    )
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )
            if comp.name == "NLA JUNIOR SENIOR":
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Starting load data to database {comp.id} -- {comp.name}"
                    )
                )
                asyncio.run(
                    load_jobtitles(
                        url=env.str("nla_jun_sen_jobs"),
                        auth=auth,
                        company=comp.name,
                        comp_id=comp.id,
                    )
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "Republic Media Limited":
                asyncio.run(
                    load_jobtitles(
                        url=env.str("repub_jobs"),
                        auth=auth,
                        company=comp.name,
                        comp_id=comp.id,
                    )
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "Rock City Professional Allowance":
                asyncio.run(
                    load_jobtitles(
                        url=env.str("rch_prof_jobs"),
                        auth=auth,
                        company=comp.name,
                        comp_id=comp.id,
                    )
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "INTU-IT GHANA LIMITED":
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )
                asyncio.run(
                    load_jobtitles(
                        url=env.str("intu_ghana_jobtitles"),
                        auth=auth,
                        company=comp.name,
                        comp_id=comp.id,
                    )
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

        self.stdout.write(self.style.SUCCESS("--------Ended Loading JobTitles-------"))

        self.stdout.write(self.style.SUCCESS("--------Loading Units-------"))
        for comp in companies:
            if comp.name == "INTERCITY STC LTD":
                self.stdout.write(
                    self.style.SUCCESS(f"Starting load data to database {comp.name}")
                )
                load_units(
                    url=env.str("intercity_sen_units"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )
                load_units(
                    url=env.str("intercity_jun_units"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

                self.stdout.write(
                    self.style.SUCCESS(f"Starting load data to database {comp.id}")
                )
                load_units(
                    url=env.str("intercity_driver_units"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "Rock City Hotel":
                self.stdout.write(
                    self.style.SUCCESS(f"Starting load data to database {comp.name}")
                )
                load_units(
                    url=env.str("rch_units"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "BRYAN ACHEAMPONG FOUNDATION":
                self.stdout.write(
                    self.style.SUCCESS(f"Starting load data to database {comp.name}")
                )
                load_units(
                    url=env.str("baf_units"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "Emery Invest":
                self.stdout.write(
                    self.style.SUCCESS(f"Starting load data to database {comp.name}")
                )
                load_units(
                    url=env.str("emery_units"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "FAAB Systems Gh. Ltd":
                self.stdout.write(
                    self.style.SUCCESS(f"Starting load data to database {comp.name}")
                )
                load_units(
                    url=env.str("faab_units"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "Rock City Hotel Heads of Department":
                self.stdout.write(
                    self.style.SUCCESS(f"Starting load data to database {comp.id}")
                )
                load_units(
                    url=env.str("rch_hod_units"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "Republic Media Limited":
                self.stdout.write(
                    self.style.SUCCESS(f"Starting load data to database {comp.id}")
                )
                load_units(
                    url=env.str("repub_units"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "Intu IT Professional Allowance":
                self.stdout.write(
                    self.style.SUCCESS(f"Starting load data to database {comp.id}")
                )
                load_units(
                    url=env.str("intuprof_units"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "INTU-IT GHANA LIMITED":
                self.stdout.write(
                    self.style.SUCCESS(f"Starting load data to database {comp.id}")
                )
                load_units(
                    url=env.str("intu_ghana_units"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "Rock City Professional Allowance":
                self.stdout.write(
                    self.style.SUCCESS(f"Starting load data to database {comp.id}")
                )
                load_units(
                    url=env.str("rch_prof_units"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )
            if comp.name == "NLA MANAGEMENT":
                self.stdout.write(
                    self.style.SUCCESS(f"Starting load data to database {comp.id}")
                )
                load_units(
                    url=env.str("nla_man_units"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )
            if comp.name == "NLA JUNIOR SENIOR":
                self.stdout.write(
                    self.style.SUCCESS(f"Starting load data to database {comp.id}")
                )
                load_units(
                    url=env.str("nla_jun_sen_units"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            self.stdout.write(
                self.style.SUCCESS(f"Starting load data to database {comp.name}")
            )

        self.stdout.write(self.style.SUCCESS("--------Loading Branches-------"))
        for comp in companies:
            if comp.name == "NLA MANAGEMENT":
                self.stdout.write(
                    self.style.SUCCESS(f"Starting load data to database {comp.id}")
                )
                load_branches(
                    url=env.str("nla_exc_man_branch"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )
            if comp.name == "NLA JUNIOR SENIOR":
                self.stdout.write(
                    self.style.SUCCESS(f"Starting load data to database {comp.id}")
                )
                load_branches(
                    url=env.str("nla_jun_sen_branch"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            self.stdout.write(
                self.style.SUCCESS(f"Starting load data to database {comp.name}")
            )

        self.stdout.write(self.style.SUCCESS("--------Loading Employees-------"))

        for company in companies:
            if company.name == "Emery Invest":
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Starting load data to database {company.id} -- {company.name}"
                    )
                )
                get_user_data(
                    url=env.str("emery"),
                    auth=auth,
                    company=company.name,
                    company_id=company.id,
                    comp_code=company.unique_code,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if company.name == "BRYAN ACHEAMPONG FOUNDATION":
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Starting load data to database {company.id} -- {company.name}"
                    )
                )
                get_user_data(
                    url=env.str("baf"),
                    auth=auth,
                    company=company.name,
                    company_id=company.id,
                    comp_code=company.unique_code,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if company.name == "FAAB Systems Gh. Ltd":
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Starting load data to database {company.id} -- {company.name}"
                    )
                )
                get_user_data(
                    url=env.str("faab"),
                    auth=auth,
                    company=company.name,
                    company_id=company.id,
                    comp_code=company.unique_code,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if company.name == "Rock City Hotel Heads of Department":
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Starting load data to database {company.id} -- {company.name}"
                    )
                )
                get_user_data(
                    url=env.str("rch_hod"),
                    auth=auth,
                    company=company.name,
                    company_id=company.id,
                    comp_code=company.unique_code,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if company.name == "REISS & CO. GHANA LIMITED":
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Starting load data to database {company.id} -- {company.name}"
                    )
                )
                get_user_data(
                    url=env.str("reiss_co"),
                    auth=auth,
                    company=company.name,
                    company_id=company.id,
                    comp_code=company.unique_code,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if company.name == "INTERCITY STC LTD":
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Starting load data to database {company.id} -- {company.name}"
                    )
                )
                get_user_data(
                    url=env.str("intercity_jun"),
                    auth=auth,
                    company=company.name,
                    company_id=company.id,
                    comp_code=company.unique_code,
                )
                get_user_data(
                    url=env.str("intercity_sen"),
                    auth=auth,
                    company=company.name,
                    company_id=company.id,
                    comp_code=company.unique_code,
                )
                get_user_data(
                    url=env.str("intercity_driver"),
                    auth=auth,
                    company=company.name,
                    company_id=company.id,
                    comp_code=company.unique_code,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if company.name == "Jays Lodge":
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Starting load data to database {company.id} -- {company.name}"
                    )
                )
                get_user_data(
                    url=env.str("jay_lodge"),
                    auth=auth,
                    company=company.name,
                    company_id=company.id,
                    comp_code=company.unique_code,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if company.name == "INTU-IT GHANA LIMITED":
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Starting load data to database {company.id} -- {company.name}"
                    )
                )
                get_user_data(
                    url=env.str("itu"),
                    auth=auth,
                    company=company.name,
                    company_id=company.id,
                    comp_code=company.unique_code,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if company.name == "Intu IT Professional Allowance":
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Starting load data to database {company.id} -- {company.name}"
                    )
                )
                get_user_data(
                    url=env.str("itu_allowance"),
                    auth=auth,
                    company=company.name,
                    company_id=company.id,
                    comp_code=company.unique_code,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if company.name == "Rock City Hotel Kumasi":
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Starting load data to database {company.id} -- {company.name}"
                    )
                )
                get_user_data(
                    url=env.str("rch_kumasi"),
                    auth=auth,
                    company=company.name,
                    company_id=company.id,
                    comp_code=company.unique_code,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if company.name == "Rock City Professional Allowance":
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Starting load data to database {company.id} -- {company.name}"
                    )
                )
                get_user_data(
                    url=env.str("rch_prof_allowance"),
                    auth=auth,
                    company=company.name,
                    company_id=company.id,
                    comp_code=company.unique_code,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if company.name == "Rock City Hotel":
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Starting load data to database {company.id} -- {company.name}"
                    )
                )
                get_user_data(
                    url=env.str("rch"),
                    auth=auth,
                    company=company.name,
                    company_id=company.id,
                    comp_code=company.unique_code,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if company.name == "Republic Media Limited":
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Starting load data to database {company.id} -- {company.name}"
                    )
                )
                get_user_data(
                    url=env.str("rml"),
                    auth=auth,
                    company=company.name,
                    company_id=company.id,
                    comp_code=company.unique_code,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if company.name == "NLA MANAGEMENT":
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Starting load data to database {company.id} -- {company.name}"
                    )
                )
                self.stdout.write(self.style.SUCCESS("----Starting Management"))
                get_user_data(
                    url=env.str("nla_man"),
                    auth=auth,
                    company=company.name,
                    company_id=company.id,
                    comp_code=company.unique_code,
                )
                self.stdout.write(self.style.SUCCESS("----Ending Management---"))
                self.stdout.write(self.style.SUCCESS("----Starting Exec Management--"))
                get_user_data(
                    url=env.str("nla_exc_man"),
                    auth=auth,
                    company=company.name,
                    company_id=company.id,
                    comp_code=company.unique_code,
                )

            if company.name == "NLA JUNIOR SENIOR":
                self.stdout.write(self.style.SUCCESS("----Starting Jun Senior-----"))
                get_user_data(
                    url=env.str("nlajun_sen"),
                    auth=auth,
                    company=company.name,
                    company_id=company.id,
                    comp_code=company.unique_code,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )
        self.stdout.write(self.style.SUCCESS("--------Ended Loading Employees-------"))

        self.stdout.write(self.style.SUCCESS("--------Loading PayGroups-------"))

        for comp in companies:
            if comp.name == "Rock City Hotel":
                self.stdout.write(
                    self.style.SUCCESS(f"Starting load data to database {comp.id}")
                )
                load_paygroup(
                    url=env.str("rchpay_group"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "BRYAN ACHEAMPONG FOUNDATION":
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Starting load data to database {comp.id} -- {comp.name}"
                    )
                )
                load_paygroup(
                    url=env.str("baf_pay_group"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "Emery Invest":
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Starting load data to database {comp.id} -- {comp.name}"
                    )
                )
                load_paygroup(
                    url=env.str("emery_pay_group"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "FAAB Systems Gh. Ltd":
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Starting load data to database {comp.id} -- {comp.name}"
                    )
                )
                load_paygroup(
                    url=env.str("faab_pay_group"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "Rock City Hotel Heads of Department":
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Starting load data to database {comp.id} -- {comp.name}"
                    )
                )
                load_paygroup(
                    url=env.str("rock_hod_pay_group"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "INTERCITY STC LTD":
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Starting load data to database {comp.id} -- {comp.name}"
                    )
                )
                load_paygroup(
                    url=env.str("intercity_jun_pay_group"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                )
                
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Starting load data to database {comp.id} -- {comp.name}"
                    )
                )
                load_paygroup(
                    url=env.str("intercity_driver_pay_group"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

                self.stdout.write(
                    self.style.SUCCESS(
                        f"Starting load data to database {comp.id} -- {comp.name}"
                    )
                )
                load_paygroup(
                    url=env.str("intercity_sen_pay_group"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "Intu IT Professional Allowance":
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Starting load data to database {comp.id} -- {comp.name}"
                    )
                )
                load_paygroup(
                    url=env.str("intuprof_allow_pay"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )
            if comp.name == "NLA":
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Starting load data to database {comp.id} -- {comp.name}"
                    )
                )
                load_paygroup(
                    url=env.str("nla_exc_man_paygroup"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )
            if comp.name == "Republic Media Limited":
                load_paygroup(
                    url=env.str("repub_paygroup"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "Rock City Professional Allowance":
                load_paygroup(
                    url=env.str("nlajun_sen_paygroup"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )

            if comp.name == "INTU-IT GHANA LIMITED":
                load_paygroup(
                    url=env.str("intu_ghana"),
                    auth=auth,
                    company=comp.name,
                    comp_id=comp.id,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully load data to database")
                )
        update_employee_record()

        self.stdout.write(self.style.SUCCESS("--------Ended Loading PayGroups-------"))

def load_sync(url, auth):
    res = requests.get(url=url, auth=auth, timeout=60)
    data = res.json()
    return data["value"]

def get_user_data(url, auth, company, company_id, comp_code):
    data = load_sync(url, auth)

    for employee in data:
        if employee["Status"] == "Active":
            print(f"{employee['No'] }- {employee['Status']}")
            logging.info(f"{employee['No']} - {employee['Status']}")
            try:
                try:
                    depart = Department.objects.get(
                        code=employee["Second_Category_Level"],
                        company_id=company_id,
                    )
                except Department.DoesNotExist:
                    depart = None

                try:
                    unit = None
                    if employee["Third_Category_Level"].strip():
                        unit = Unit.objects.get(
                            code=employee["Third_Category_Level"],
                            company=company,
                            department=depart,
                        )
                except Unit.DoesNotExist:
                    unit = None

                try:
                    branch_code = employee["Fourth_Category_Level"].strip()
                    if branch_code:
                        branch = Branch.objects.get(code=branch_code, company=company)
                    else:
                        branch = None
                except ObjectDoesNotExist:
                    branch = None

                if Employee.objects.filter(
                    code=employee["No"], company=company
                ).exists():
                    employee_obj = Employee.objects.get(
                        code=employee["No"], company=company
                    )
                    logging.info(
                        f"--updating-- {employee_obj} --- Department -- {employee['Second_Category_Level']}"
                    )
                    Employee.objects.filter(id=employee_obj.id).update(
                        code=employee["No"],
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
                        department=depart
                        if employee["Second_Category_Level"].strip() != ""
                        else None,
                        unit=unit
                        if employee["Third_Category_Level"].strip() != ""
                        else None,
                        branch=branch
                        if employee["Fourth_Category_Level"].strip() != ""
                        else None,
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
                        contribute_to_ssf_employee=employee[
                            "Contribute_to_SSF_Employee"
                        ],
                        contribute_to_ssf_employer=employee[
                            "Contribute_to_SSF_Employer"
                        ],
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
                        company_id=Company.objects.get(id=company_id),
                        unique_code=comp_code,
                    )
                if (
                    not Employee.objects.filter(
                        code=employee["No"], company=company
                    ).exists()
                    and Department.objects.filter(
                        code=employee["Second_Category_Level"], company_id=company_id
                    ).exists()
                ):
                    logging.info(
                        f"--creating-- {employee['No']} --- Department Code -- {employee['Third_Category_Level']} -- {comp_code}"
                    )

                    Employee.objects.create(
                        code=employee["No"],
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
                        department=depart
                        if employee["Second_Category_Level"].strip() != ""
                        else None,
                        unit=unit
                        if employee["Third_Category_Level"].strip() != ""
                        else None,
                        branch=branch
                        if employee["Fourth_Category_Level"].strip() != ""
                        else None,
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
                        contribute_to_ssf_employee=employee[
                            "Contribute_to_SSF_Employee"
                        ],
                        contribute_to_ssf_employer=employee[
                            "Contribute_to_SSF_Employer"
                        ],
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
                        company_id=Company.objects.get(id=company_id),
                        unique_code=comp_code,
                    )
                print(f"Ending -- Employee {employee['No']}")
            except Employee.DoesNotExist:
                logging.info(f"--Doesn't-- {employee['No']}")




# async def load_paygroup(url, auth, company, comp_id):
#     data = load_sync(url, auth)

#     for paygroup in data:
#         no = paygroup["No"].strip()
#         description = paygroup["Description"].strip()
#         taxable_income_code = paygroup["Taxable_Income_Code"].strip()
#         taxable_income_description = paygroup["Taxable_Income_Description"].strip()
#         tax_code = paygroup["Tax_Code"].strip()
#         tax_description = paygroup["Tax_Description"].strip()
#         gross_income_code = paygroup["Gross_Income_Code"].strip()
#         gross_income_description = paygroup["Gross_Income_Description"].strip()
#         currency_code = paygroup["Currency_Code"].strip()
#         bonus_tax_code = paygroup["Bonus_Tax_Code"].strip()
#         bonus_tax_description = paygroup["Bonus_Tax_Description"].strip()
#         gross_up = paygroup["Gross_Up"].strip()

#         company_instance = await sync_to_async(Company.objects.get)(id=comp_id)

#         pg, created = await sync_to_async(PayGroup.objects.get_or_create)(
#             no=no,
#             company=company,
#             defaults={
#                 "description": description,
#                 "taxable_income_code": taxable_income_code,
#                 "taxable_income_description": taxable_income_description,
#                 "tax_code": tax_code,
#                 "tax_description": tax_description,
#                 "gross_income_code": gross_income_code,
#                 "gross_income_description": gross_income_description,
#                 "currency_code": currency_code,
#                 "bonus_tax_code": bonus_tax_code,
#                 "bonus_tax_description": bonus_tax_description,
#                 "gross_up": gross_up,
#                 "comp_id": company_instance,
#             },
#         )

#         if not created:
#             pg.description = description
#             pg.taxable_income_code = taxable_income_code
#             pg.taxable_income_description = taxable_income_description
#             pg.tax_code = tax_code
#             pg.tax_description = tax_description
#             pg.gross_income_code = gross_income_code
#             pg.gross_income_description = gross_income_description
#             pg.currency_code = currency_code
#             pg.bonus_tax_code = bonus_tax_code
#             pg.bonus_tax_description = bonus_tax_description
#             pg.gross_up = gross_up
#             pg.comp_id = company_instance
#             await sync_to_async(pg.save)()

def load_paygroup(url, auth, company, comp_id):
    data = load_sync(url, auth)

    for paygroup in data:
        try:
            if PayGroup.objects.filter(no=paygroup["No"], company=company).exists():
                paygroup_id = PayGroup.objects.get(no=paygroup["No"], company=company)
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
                    comp_id=Company.objects.get(id=comp_id),
                )
            elif not PayGroup.objects.filter(
                no=paygroup["No"], company=company
            ).exists():
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
                    comp_id=Company.objects.get(id=comp_id),
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
                comp_id=Company.objects.get(id=comp_id),
            )


async def load_department(url, auth, company, comp_id):
    data = load_sync(url, auth)

    for dep in data:
        code = dep["Code"].strip()
        name = dep["Name"].strip()
        first_category_code = dep["First_Category_Code"].strip()

        company_instance = await sync_to_async(Company.objects.get)(id=comp_id)
        department, created = await sync_to_async(Department.objects.get_or_create)(
            code=code,
            company=company,
            defaults={
                "name": name,
                "first_category_code": first_category_code,
                "company_id": comp_id,
                "comp_id": company_instance,
            },
        )

        if not created:
            department.name = name
            department.first_category_code = first_category_code
            department.company_id = comp_id
            department.comp_id = company_instance
            await sync_to_async(department.save)()


def load_units(url, auth, company, comp_id):
    data = load_sync(url, auth)

    for unit in data:
        try:
            try:
                depart = Department.objects.get(
                    code=unit["Second_Category_Code"],
                    company_id=comp_id,
                )
            except Department.DoesNotExist:
                depart = None
            if Unit.objects.filter(code=unit["Code"], company=company).exists():
                unit_id = Unit.objects.get(code=unit["Code"], company=company)
                print("Updating Existing Unit")
                Unit.objects.filter(code=unit_id).update(
                    code=unit["Code"].strip(),
                    name=unit["Name"].strip(),
                    department=depart
                    if unit["Second_Category_Code"].strip() != ""
                    else None,
                    comp_id=Company.objects.get(id=comp_id),
                    company=company.strip(),
                    company_id=comp_id,
                )
            elif not Unit.objects.filter(code=unit["Code"], company=company).exists():
                logging.info(
                    f"--Creating New Unit--- Unit -- {unit['Code']} -- Company {company}"
                )
                if depart:
                    Unit.objects.create(
                        code=unit["Code"].strip(),
                        name=unit["Name"].strip(),
                        department=depart
                        if unit["Second_Category_Code"].strip() != ""
                        else None,
                        comp_id=Company.objects.get(id=comp_id),
                        company=company.strip(),
                        company_id=comp_id,
                    )
                else:
                    logging.info(
                        f"{unit['Second_Category_Code']} -- {company} Not Found"
                    )
        except Unit.DoesNotExist:
            logging.info(f"Unit {unit['Second_Category_Code']} -- {company} Not Found")


def load_branches(url, auth, company, comp_id):
    data = load_sync(url, auth)

    for branch in data:
        try:
            try:
                unit = Unit.objects.get(
                    code=branch["Third_Category_Code"].strip(),
                    company_id=comp_id,
                )
            except Unit.DoesNotExist:
                unit = None
            if Branch.objects.filter(code=branch["Code"], company=company).exists():
                unit_id = Branch.objects.get(code=branch["Code"], company=company)
                print("Updating Existing Unit")
                Branch.objects.filter(code=unit_id).update(
                    code=branch["Code"].strip(),
                    name=branch["Name"].strip(),
                    unit=unit if branch["Third_Category_Code"].strip() != "" else None,
                    comp_id=Company.objects.get(id=comp_id),
                    company=company.strip(),
                    company_id=comp_id,
                )
            elif not Branch.objects.filter(
                code=branch["Code"], company=company
            ).exists():
                print("--Creating New Unit---")
                Branch.objects.create(
                    code=branch["Code"].strip(),
                    name=branch["Name"].strip(),
                    unit=unit if branch["Third_Category_Code"].strip() != "" else None,
                    comp_id=Company.objects.get(id=comp_id),
                    company=company.strip(),
                    company_id=comp_id,
                )
        except Branch.DoesNotExist:
            logging.info(f"Branch {branch['Third_Category_Code']} -- Does not exist")


async def load_jobtitles(url, auth, company, comp_id):
    data = load_sync(url=url, auth=auth)

    for val in data:
        code = val["Code"].strip()
        description = val["Description"].strip()
        if code != "CODE":
            company_instance = await sync_to_async(Company.objects.get)(id=comp_id)

            job, created = await sync_to_async(JobTitles.objects.get_or_create)(
                code=code,
                company=company,
                defaults={
                    "description": description,
                    "company_id": company_instance,
                },
            )

            if not created:
                job.description = description
                job.company_id = company_instance
                await sync_to_async(job.save)()


def update_employee_record():
    # Send email report
    try:
        print("---------------Sending -----------------------")
        # send_mail(subject, message, from_email, recipient_list)
        # print("---------------Sent -----------------------")
        subject = "Report"
        message = "The task has been completed successfully."
        from_email = "justiceduodu14@gmail.com"
        recipient_list = [
            "justicemclean@proton.me",
        ]

        send_mail(subject, message, from_email, recipient_list)
        print("---------------Sent -----------------------")
    except:
        print("-----------------Couldn't send------------------------")