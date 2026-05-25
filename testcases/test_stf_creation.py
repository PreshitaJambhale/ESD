import time

import pytest

from pages.Internal_stf import InternalSTF
from pages.multiple_line_items_stf import MultipleLineItems
from pages.stf_approval import StfApproval
from pages.stf_create_page import StfCreation


@pytest.mark.usefixtures("setup")
class Test_STF():

    def test_stf_create(self):
         sc = StfCreation(self.driver)
         sc.log_in("admin", "test")
         sc.stf_visibilty()
         sc.stf_create_func()
         sc.stf_customer_contacts()
         #sc.product1()
         sc.multiple_products()

         sc.send_for_approval()



    def test_stf_create3(self):
         sc = StfCreation(self.driver)
         sc.log_in("admin", "test")
         sc.stf_visibilty()
         sc.stf_create_func()
         sc.stf_customer_contacts()
         # sc.product1()
         sc.multiple_products()

         sc.send_for_approval()

    def test_stf_create4(self):
         sc = StfCreation(self.driver)
         sc.log_in("admin", "test")
         sc.stf_visibilty()
         sc.stf_create_func()
         sc.stf_customer_contacts()
         # sc.product1()
         sc.multiple_products()
         sc.send_for_approval()
     #sc.get_stf_id()



    '''
    def test_stf_approval(self):
        sc = StfCreation(self.driver)

        sc.log_in("gsurve", "test")
        sa = StfApproval(self.driver)
        time.sleep(5)
        sa.stf_visibilty()
        time.sleep(5)
        sa.handles_windows()
        sa.stf_approval()
        sc.log_in("gsurve", "test")
        sc.
    

  

    def test_multiple_line_items(self):
        sc= StfCreation(self.driver)
        sc.log_in("admin", "test")
        sc.stf_visibilty()
        sc.stf_create_func()
        sc.stf_customer_contacts()
        mi = MultipleLineItems(self.driver)
        mi.multiple_line_items(20)
        sc.send_for_approval()

    
    def test_Internal_stf(self):
        Is = InternalSTF(self.driver)
        sc = StfCreation(self.driver)
        sc.log_in("admin", "test")
        sc.stf_visibilty()
        Is.customer_details()
        sc.stf_customer_contacts()
        Is.multiple_products()
        sc.send_for_approval()


    def test_stf_approval(self):
        sc = StfCreation(self.driver)

        sc.log_in("gsurve", "test")
        sa = StfApproval(self.driver)
        time.sleep(5)
        sa.stf_visibilty()
        time.sleep(5)
        sa.handles_windows()
        sa.stf_approval()
        sc.log_in("gsurve", "test")

'''
    def test_stf_create2(self):
         sc = StfCreation(self.driver)
         sc.log_in("admin", "test")
         sc.stf_visibilty()
         sc.stf_create_func()
         sc.stf_customer_contacts()
         #sc.product1()
         sc.multiple_products()

         sc.send_for_approval()