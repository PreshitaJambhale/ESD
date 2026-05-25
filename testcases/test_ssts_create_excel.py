

import time


import pytest

import os



from base.Base_file1 import BaseDriver
from pages.sstf_create_page import sstf_create
from utilities.ddt_with_excel import utils




@pytest.mark.usefixtures("setup")
class Test_py():
    rows = utils().read_data_from_excel(
        "/Users/harshalijambhale/eclipse-workspace/test/src/test/resources/testngData.xlsx", "Sheet1")

    @pytest.mark.parametrize(
        ("username", "password", "sales_ex_name", "sales_spe_name", "prod_group_name", "regularization_name",
         "branch_name", "customer_name", "sbu_name", "principal_name", "product_name", "hsn_code",
         "quantity", "selling_price", "cost_price", "fullfilment_type_name", "fulfilment_team_name",
         "service_type_name",
         "billing_type_name"), rows)
    def test_2(self, username, password, sales_ex_name, sales_spe_name, prod_group_name, regularization_name,
                 branch_name, customer_name, sbu_name, principal_name, product_name, hsn_code,
                 quantity, selling_price, cost_price, fullfilment_type_name, fulfilment_team_name, service_type_name,
                 billing_type_name):
        cp = sstf_create(self.driver)
        cp.create_page(username, password, sales_ex_name, sales_spe_name, prod_group_name, regularization_name,
                       branch_name, customer_name, sbu_name, principal_name, product_name, hsn_code,
                       quantity, selling_price, cost_price, fullfilment_type_name, fulfilment_team_name,
                       service_type_name,
                       billing_type_name)





    """
    rows = utils().read_data_from_excel("/Users/harshalijambhale/eclipse-workspace/test/src/test/resources/testngData.xlsx", "Sheet1")
  
    file = "/Users/harshalijambhale/eclipse-workspace/test/src/test/resources/testngData.xlsx"



    @pytest.mark.parametrize("username","password", rows)
    def test_1(self,username, password):
        cp = sstf_create(self.driver)

        cp.log_in(username, password)

        cp.sstf_visibilty()


    @pytest.mark.parametrize("sales_ex_name","sales_spe_name","prod_group_name","regularization_name",rows)
    def test_2(self, sales_ex_name, sales_spe_name, prod_group_name, regularization_name):
        cp = sstf_create(self.driver)
        cp.sstf_basic_info(sales_ex_name, sales_spe_name, prod_group_name, regularization_name)

    @pytest.mark.parametrize("branch_name","customer_name", rows)
    def test_3(self, branch_name, customer_name):
        cp = sstf_create(self.driver)
        cp.basic_details(branch_name, customer_name)
        cp.sstf_calander()
        cp.customer_names()
        cp.add_address()
        document = os.path.abspath("/Users/harshalijambhale/Documents/Book1.xlsx")
        cp.add_docs(document)
        time.sleep(2)

    @pytest.mark.parametrize("sbu_name","principal_name","product_name","hsn_code","quantity",
        "selling_price","cost_price,"
        "fullfilment_type_name","fulfilment_team_name","service_type_name","billing_type_name",rows)
    def test_4(self,sbu_name, principal_name, product_name, hsn_code, quantity, selling_price, cost_price,
                   fullfilment_type_name, fulfilment_team_name, service_type_name, billing_type_name):
        cp = sstf_create(self.driver)
        cp.product(sbu_name, principal_name, product_name, hsn_code, quantity, selling_price, cost_price,
                   fullfilment_type_name, fulfilment_team_name, service_type_name, billing_type_name)
        cp.add_more_products()
        # time.sleep(2)
        # cp.another_line_item(2,"Synergy", "Remote Management Services", "Firewall Remote Management Services", 1, 10 , 450000, 400000,"Internal", 1, "New", "One Time", "GST" )
        # cp.add_more_products()
        # cp.another_line_item(3,"Synergy", "Remote Management Services", "Firewall Remote Management Services", 1, 10 , 450000, 400000, "Internal", 1, "New", "One Time", "GST")
        cp.send_for_approval()
        
        
     """

@pytest.mark.usefixtures("setup")
class Test_py2():
    pass






