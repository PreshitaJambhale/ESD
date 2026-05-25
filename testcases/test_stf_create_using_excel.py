

import time


import pytest

import os



from base.Base_file1 import BaseDriver
from pages.sstf_create_page import sstf_create
from pages.stf_create_using_excel import ExcelSTF
from utilities.ddt_with_excel import utils

@pytest.mark.usefixtures("setup")
class Test_py():
    rows = utils().read_data_from_excel(
        "/Users/harshalijambhale/Downloads/test sheets/subscription_stf_create_data.xlsx", "Sheet1")

    @pytest.mark.parametrize(
        ("username", "password", "iss", "sales_specialist", "tech_role", "other_sales", "stf_type", "regularization_path", "branch",
         "customer_name", "program_type", "month", "year",
         "customer_contact_id", "sbu", "principle", "product",
         "quantity", "selling_price", "cost_price", "product_type", "billing_cycle",
         "period", "billing_branch"), rows)
    def test_subsciption_line_item1(self, username,password ,iss, sales_specialist, tech_role, other_sales, stf_type, regularization_path, branch, customer_name, program_type,month, year,customer_contact_id,sbu, principle, product, quantity, selling_price, cost_price, product_type, billing_cycle, period, billing_branch):
        es = ExcelSTF(self.driver)
        es.subscription_stf(username,password ,iss, sales_specialist, tech_role, other_sales, stf_type, regularization_path, branch, customer_name, program_type,month, year,customer_contact_id,sbu, principle, product, quantity, selling_price, cost_price, product_type, billing_cycle, period, billing_branch)