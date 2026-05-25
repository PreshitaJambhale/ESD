import os

import pytest

from pages.sstf_create_page import sstf_create

from utilities.ddt_with_json import read_json


@pytest.mark.usefixtures("setup")
class Test_with_json():

    def test_sstf_create(self):
        data = read_json("/Users/harshalijambhale/PycharmProjects/frameworkmaintainance/data/sstf_create.json")

        cp = sstf_create(self.driver)

        cp.log_in(
            data["login"]["username"],
            data["login"]["password"]
        )

        cp.sstf_visibilty()

        cp.sstf_basic_info(
            data["basic_info"]["sales_ex_name"],
            data["basic_info"]["sales_spe_name"],
            data["basic_info"]["prod_group_name"],
            data["basic_info"]["regularization_name"]
        )

        cp.basic_details(
            data["customer"]["branch_name"],
            data["customer"]["customer_index"]
        )

        cp.sstf_calander()
        cp.customer_names()
        cp.add_address()
        document = os.path.abspath("/Users/harshalijambhale/Documents/Book1.xlsx")
        cp.add_docs(document)

        for product in data["products"]:
            cp.product(
                product["sbu_name"],
                product["principal_name"],
                product["product_name"],
                product["hsn_code"],
                product["quantity"],
                product["selling_price"],
                product["cost_price"],
                product["fulfilment_type_name"],
                product["fulfilment_team_name"],
                product["service_type_name"],
                product["billing_type_name"]
            )

        cp.add_more_products()

        for line_item in data["second_line_item"]:
            cp.another_line_item(
                line_item["current_value"],
                line_item["sbu_name"],
                line_item["principal_name"],
                line_item["product_name"],
                line_item["hsn_code"],
                line_item["quantity"],
                line_item["selling_price"],
                line_item["cost_price"],
                line_item["fulfilment_type_name"],
                line_item["fulfilment_team_name"],
                line_item["service_type_name"],
                line_item["billing_type_name"],
                line_item["ISD_name"]
            )
        cp.add_more_products()

        for line_item in data["third_line_item"]:
            cp.another_line_item(
                line_item["current_value"],
                line_item["sbu_name"],
                line_item["principal_name"],
                line_item["product_name"],
                line_item["hsn_code"],
                line_item["quantity"],
                line_item["selling_price"],
                line_item["cost_price"],
                line_item["fulfilment_type_name"],
                line_item["fulfilment_team_name"],
                line_item["service_type_name"],
                line_item["billing_type_name"],
                line_item["ISD_name"]
            )
        cp.add_more_products()

        for line_item in data["fourth_line_item"]:
            cp.another_line_item(
                line_item["current_value"],
                line_item["sbu_name"],
                line_item["principal_name"],
                line_item["product_name"],
                line_item["hsn_code"],
                line_item["quantity"],
                line_item["selling_price"],
                line_item["cost_price"],
                line_item["fulfilment_type_name"],
                line_item["fulfilment_team_name"],
                line_item["service_type_name"],
                line_item["billing_type_name"],
                line_item["ISD_name"]
            )



        cp.send_for_approval()

        print("success")
