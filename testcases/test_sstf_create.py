
import time


import pytest

import os



from base.Base_file1 import BaseDriver
from pages.sstf_create_page import sstf_create
from utilities.ddt_with_excel import utils




@pytest.mark.usefixtures("setup")
class Test_py():

    def test_1(self):
        cp = sstf_create(self.driver)

        cp.log_in("admin", "test")

        cp.sstf_visibilty()
        cp.sstf_basic_info("Harshali Jambhale", "Harshali Jambhale", "SI", "No")
        cp.basic_details("Mumbai", 4)
        cp.sstf_calander()
        cp.customer_names()
        cp.add_address()
        document = os.path.abspath("/Users/harshalijambhale/Documents/Book1.xlsx")
        cp.add_docs(document)
        time.sleep(2)
        cp.product("Synergy","Remote Management Services","Firewall Remote Management Services",2, 10, 30000, 25000, "Internal", "Ongoing Support", "Renewal", "One Time" )
        cp.add_more_products()
        #time.sleep(2)
        cp.another_line_item(2,"Synergy", "Remote Management Services", "Firewall Remote Management Services", 2, 10 , 450000, 400000,"External", "Ongoing Support", "New", "One Time", "GST" )
        cp.add_more_products()
        cp.another_line_item(3,"Synergy", "Remote Management Services", "Firewall Remote Management Services", 2, 10 , 450000, 400000, "Internal", "Ongoing Support", "New", "One Time", "GST")
        cp.add_supplier_po_to_be_raised_from("Mumbai")
        cp.send_for_approval()
        #cp.click_search

