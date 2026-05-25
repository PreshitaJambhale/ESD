import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import random
from datetime import date
import os

from utilities.utils_for_stf import Utils


class sstf_create():
    current_value = 1
    login_path = (By.XPATH, "//input[@id='username']")
    password_path = (By.XPATH, "//input[@id='password']")
    admit_path = (By.XPATH, "//button[normalize-space()='Log in']")
    logout_toggle = (By.XPATH, "//a[@class='user-profile dropdown-toggle']//i[@class='fa fa-briefcase']")
    logout_path = (By.XPATH, "//a[normalize-space()='Log Out']")
    wc_path = (By.XPATH, "//a[@id='menu_toggle']")
    sstf_icon_path = (By.XPATH, "//a[@href='/sstf/']")
    sstf_create_path = (By.XPATH, "//a[@href='/sstf/create.html']//div[@class='service-icon']")
    sales_ex_path = (By.XPATH, "//select[@name='sstf[basic][iam_iss]']")
    sales_spe_path = (By.XPATH, "//select[@name='sstf[basic][sales_specialist]']")
    prod_group_path = (By.XPATH, "//select[@name='sstf[basic][product_group]']")
    regularization_path = (By.XPATH, "//select[@name='sstf[basic][is_regularization]']")
    branch_path = (By.XPATH, "//select[@id='branch']")
    customer_name_path = (By.XPATH, "//select[@name='sstf[customer][id]']")
    customer_po_path = (By.XPATH, "//input[@name='sstf[customer][po_no]']")
    customer_po_calander_path = (By.XPATH, "//input[@name='sstf[customer][date_po]']")
    received_po_calander_xpath = (By.XPATH, "//input[@name='sstf[customer][date_po_receive]']")
    customer1_path = (By.XPATH, "//select[@name='sstf[contacts][po_placed][1][id]']")
    customer1_name = (By.XPATH, "//input[@name='sstf[contacts][po_placed][1][landline_number]']")
    customer2_path = (By.XPATH, "//select[@name='sstf[contacts][cordinator][1][id]']")
    customer3_path = (By.XPATH, "//select[@name='sstf[contacts][po_followup][1][id]']")
    address_path = (By.XPATH, "/html/body/div[2]/div[1]/div[3]/div/form/div[2]/div[6]/div/div[2]/div/div[2]/label[2]/div")
    final_quote_path = (By.XPATH, "//input[@name='doc-final-quote[]']")
    customer_po_doc_path = (By.XPATH, "//input[@name='doc-po[]']")
    workscope_doc_path = (By.XPATH, "//input[@name='doc-work-scope[]']")

    #product paths
    sbu_path = (By.XPATH, f"//select[@name='sstf[product][{current_value}][sbu_id]']")
    principal_path = (By.XPATH, f"//select[@name='sstf[product][{current_value}][principal_id]']")
    prod_name_path = (By.XPATH, f"//input[@name = 'sstf[product][{current_value}][name]']")
    prod_search_button_path = (By.XPATH, "//button[normalize-space()='Search!']")
    prod_placeholder_path = (By.XPATH, "//input[@placeholder='Search for...']")
    first_item_path = (By.XPATH, "//body[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/table[1]/tbody[1]/tr[1]/td[2]/a[1]")
    HSN_path =(By.XPATH, f"//select[@name='sstf[product][{current_value}][hsn_sac_code]']")
    quant_path = (By.XPATH, f"//input[@name='sstf[product][{current_value}][quantity]']")
    selling_price_path = (By.XPATH, f"//input[@name='sstf[product][{current_value}][selling_price]']")
    cost_price_path = (By.XPATH, f"//input[@name='sstf[product][{current_value}][cost_price]']")
    arrow_collapse_path = (By.XPATH, "//div[@class='arrow additional-collapse cursor']")

    fulfilment_team_path = (By.XPATH, f"//select[@name='sstf[product][{current_value}][fulfilment_type]']")
    fulfilment_type_path =(By.XPATH, f"//select[@name='sstf[product][{current_value}][team]']")
    service_type_path = (By.XPATH, f"//select[@name='sstf[product][{current_value}][service_type]']")
    billing_type_path = (By.XPATH, f"//select[@name='sstf[product][{current_value}][billing_type]']")
    expected_date_calander_path = (By.XPATH, f"//input[@name='sstf[product][{current_value}][expected_fulfillment_date]']")
    expected_date_path = (By.XPATH,"(//td[@class='available active start-date end-date'][normalize-space()='33'])[1]")
    add_more_path = (By.XPATH, "//div[@class='col-md-12 col-sm-12 col-xs-12 form-group']//button[@type='button'][normalize-space()='Add More']")

    ISD_path = (By.XPATH, f"//select[@name='sstf[product][{current_value}][isd_gst_type]']")



    approval_path = (By.XPATH, "//button[normalize-space()='Send for Approval']")

    """documents"""
    document = os.path.abspath("/Users/harshalijambhale/Documents/Book1.xlsx")


    """new"""
    search_sstf_path = (By.XPATH, "/html/body/div[2]/div/div[3]/div/div/div[2]/div[3]/a")

    def __init__(self,driver):
        self.driver = driver
        self.Wait = WebDriverWait(driver, 20)
        self.uc = Utils(self.driver)



    def open_url(self, url):
        self.driver.get(url)

    def log_in(self, username, password):
        self.driver.find_element(*self.login_path).send_keys(username)
        self.driver.find_element(*self.password_path).send_keys(password)
        #self.driver.find_element(*self.admit_path).click()
        self.Wait.until(EC.element_to_be_clickable(self.admit_path)).click()


    def log_out(self):
        self.driver.find_element(*self.logout_toggle).click()
        self.driver.find_element(*self.logout_path).click()

    #def welcome_text(self):
       # check.is_true(self.check_element_present(self.wc_path),
          #    "Welcome text is not visible")

    def sstf_visibilty(self):
        time.sleep(2)
        self.driver.find_element(*self.sstf_icon_path).click()
        self.driver.find_element(*self.sstf_create_path).click()

    def sstf_basic_info(self, sales_ex_name, sales_spe_name, prod_group_name, regularization_name):
       sales_ex = Select(self.driver.find_element(*self.sales_ex_path))
       #check.is_true(self.check_option_present(self.sales_ex_path,"John Doe" ),"Dropdown option 'John Doe' not found inside Sales Executive dropdown")
       sales_ex.select_by_visible_text(sales_ex_name)
       sales_spe = Select(self.driver.find_element(*self.sales_spe_path))
       sales_spe.select_by_visible_text(sales_spe_name)
       prod_grp = Select(self.driver.find_element(*self.prod_group_path))
       prod_grp.select_by_visible_text(prod_group_name)
       regularization = Select(self.driver.find_element(*self.regularization_path))
       regularization.select_by_visible_text(regularization_name)

    def random_number_generator(self):
        random_number = random.randint(1, 500000)
        return (f'automated_sstf_' + str(random_number))

    def basic_details(self, branch_name, customer_name):
        branch = Select(self.driver.find_element(*self.branch_path))
        branch.select_by_visible_text(branch_name)
        customer_name_dd = Select(self.driver.find_element(*self.customer_name_path))

        customer_name_dd.select_by_index(customer_name)
        self.driver.find_element(*self.customer_po_path).send_keys(self.random_number_generator())



    def sstf_calander(self):
        print(self.principal_path)
        today = date.today()
        current_date = today.day
        print(f"Today's date: {today} , {current_date}")
        self.driver.find_element(*self.customer_po_calander_path).click()
        customer_po_date = "body > div:nth-child(7) > div:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1)"
        self.uc.handle_click((By.CSS_SELECTOR, customer_po_date))
        selected_customer_po_date = self.driver.find_element(*self.customer_po_calander_path).get_attribute("value")
        self.driver.find_element(*self.received_po_calander_xpath).click()
        received_po_date = "body > div:nth-child(8) > div:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(1)"
        self.uc.handle_click((By.CSS_SELECTOR, received_po_date))
        selected_received_po_date = self.driver.find_element(*self.received_po_calander_xpath).get_attribute("value")
        return selected_customer_po_date, selected_received_po_date, current_date



    def customer_names(self):
        customer1 =  Select(self.driver.find_element(*self.customer1_path))
        customer1.select_by_index(1)
        self.Wait.until(EC.element_to_be_clickable(self.customer1_name)).send_keys("1234567890")
        customer2 = Select(self.driver.find_element(*self.customer2_path))
        customer2.select_by_index(1)
        customer3 = Select(self.driver.find_element(*self.customer3_path))
        customer3.select_by_index(1)
        time.sleep(2)

    def add_address(self):
        self.driver.find_element(*self.address_path).click()

    def add_docs(self, document):

        self.driver.find_element(*self.final_quote_path).send_keys(document)
        self.driver.find_element(*self.customer_po_doc_path).send_keys(document)
        self.driver.find_element(*self.workscope_doc_path).send_keys(document)


    def product(self, sbu_name,principal_name,product_name,hsn_code, quantity, selling_price, cost_price, fullfilment_type_name, fulfilment_team_name, service_type_name, billing_type_name):
        sbu = Select(self.driver.find_element(*self.sbu_path))
        sbu.select_by_visible_text(sbu_name)
        principal = Select(self.driver.find_element(*self.principal_path))
        principal.select_by_visible_text(principal_name)
        self.driver.find_element(*self.prod_name_path).click()

        self.Wait.until(EC.element_to_be_clickable(self.prod_search_button_path)).click()
        self.driver.find_element(*self.prod_placeholder_path).send_keys(product_name)
        self.Wait.until(EC.element_to_be_clickable(self.first_item_path)).click()
        HSN = Select(self.driver.find_element(*self.HSN_path))
        HSN.select_by_index(hsn_code)
        self.driver.find_element(*self.quant_path).send_keys(quantity)
        self.driver.find_element(*self.selling_price_path).send_keys(selling_price)
        self.driver.find_element(*self.cost_price_path).send_keys(cost_price)
        time.sleep(2)
        self.driver.find_element(*self.arrow_collapse_path).click()

        fullfilment_type = Select(self.driver.find_element(*self.fulfilment_type_path))
        fullfilment_type.select_by_visible_text(fullfilment_type_name)

        fulfilment_team = Select(self.driver.find_element(*self.fulfilment_team_path))
        fulfilment_team.select_by_visible_text(fulfilment_team_name)

        service_type = Select(self.driver.find_element(*self.service_type_path))
        service_type.select_by_visible_text(service_type_name)
        billing_type = Select(self.driver.find_element(*self.billing_type_path))
        billing_type.select_by_visible_text(billing_type_name)
        self.driver.find_element(*self.expected_date_calander_path).click()
        today = date.today()
        current_date = today.day
        print(10)
        #expected_date =f"(//td[contains(text(),'{current_date}')])[1]"
        expected_date = "body > div:nth-child(6) > div:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(6) > td:nth-child(7)"

        print(expected_date)
        self.Wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, expected_date))).click()
        print(2)


        #ISD = Select(self.driver.find_element(*self.ISD_path))
        #ISD.select_by_visible_text(ISD_name)


    def add_more_products(self):
        self.driver.find_element(*self.add_more_path).click()
        print(2)


    def more_products(self, number_of_items, sbu_name):
        for i in range(number_of_items):
            path1 = self.sbu_path
            sbu = Select(self.driver.find_element(*path1))
            sbu.select_by_visible_text(sbu_name)
            self.current_value +=1
            i+=1
            time.sleep(2)
            print(path1)

    def another_line_item(self,current_value,sbu_name,principal_name,product_name,hsn_code, quantity, selling_price, cost_price, fulfillment_team_name, fulfillment_type_name, service_type_name, billing_type_name, ISD_name):

        sbu = Select(self.driver.find_element(By.XPATH, f"//select[@name='sstf[product][{current_value}][sbu_id]']"))
        sbu.select_by_visible_text(sbu_name)
        print(sbu)
        principal = Select(self.driver.find_element(By.XPATH, f"//select[@name='sstf[product][{current_value}][principal_id]']"))
        principal.select_by_visible_text(principal_name)
        self.driver.find_element(By.XPATH, f"//input[@name = 'sstf[product][{current_value}][name]']").click()
        self.uc.handle_send_keys((By.XPATH, "//input[@placeholder='Search for...']"), product_name)
        self.uc.handle_click((By.XPATH, "//button[normalize-space()='Search!']"))
        self.Wait.until(EC.element_to_be_clickable((By.XPATH, "//body[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/table[1]/tbody[1]/tr[1]/td[2]/a[1]"))).click()
        HSN = Select(self.driver.find_element(By.XPATH, f"//select[@name='sstf[product][{current_value}][hsn_sac_code]']"))
        HSN.select_by_index(hsn_code)
        self.driver.find_element(By.XPATH, f"//input[@name='sstf[product][{current_value}][quantity]']").send_keys(quantity)
        self.driver.find_element(By.XPATH, f"//input[@name='sstf[product][{current_value}][selling_price]']").send_keys(selling_price)
        self.driver.find_element(By.XPATH, f"//input[@name='sstf[product][{current_value}][cost_price]']").send_keys(cost_price)
        self.driver.find_element(By.XPATH, "//div[@class='arrow additional-collapse cursor']").click()


        #self.uc.handle_drop_down((By.XPATH, f"//select[@name='sstf[product][{current_value}][team]']"), fulfillment_team_name)
        fullfilment_type = Select(self.Wait.until(EC.element_to_be_clickable((By.XPATH, f"//select[@name='sstf[product][{current_value}][team]']"))))
        fullfilment_type.select_by_visible_text(fulfillment_team_name)

        #self.uc.handle_drop_down((By.XPATH, f"//select[@name='sstf[product][{current_value}][fulfilment_type]']"), fulfillment_type_name)
        fulfilment_team = Select(self.Wait.until(EC.element_to_be_clickable((By.XPATH, f"//select[@name='sstf[product][{current_value}][fulfilment_type]']"))))
        fulfilment_team.select_by_visible_text(fulfillment_type_name)

        service_type = Select(self.driver.find_element(By.XPATH, f"//select[@name='sstf[product][{current_value}][service_type]']"))
        service_type.select_by_visible_text(service_type_name)
        billing_type = Select(self.driver.find_element(By.XPATH, f"//select[@name='sstf[product][{current_value}][billing_type]']"))
        billing_type.select_by_visible_text(billing_type_name)
        self.driver.find_element(By.XPATH, f"//input[@name='sstf[product][{current_value}][expected_fulfillment_date]']").click()
        div_index = 3 + (current_value * 5)
        selector = f"body > div:nth-child({div_index}) > div:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(6) > td:nth-child(7)"

        self.uc.handle_click((By.CSS_SELECTOR, selector))

        print(2)

        ISD = Select(self.driver.find_element(By.XPATH, f"//select[@name='sstf[product][{current_value}][isd_gst_type]']"))
        ISD.select_by_visible_text(ISD_name)

    def add_supplier_po_to_be_raised_from(self, branch_po):
        supplier_branch = Select(self.Wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@name='sstf[customer][po_to_raised_from]']"))))
        supplier_branch.select_by_visible_text(branch_po)


    def send_for_approval(self):
        self.Wait.until(EC.element_to_be_clickable(self.approval_path)).click()
        print(20)

    def click_search(self):
        self.Wait.until(EC.element_to_be_clickable(self.search_sstf_path)).click()
        print(20)

    def create_page(self, username, password,sales_ex_name, sales_spe_name, prod_group_name, regularization_name, branch_name, customer_name, sbu_name, principal_name, product_name, hsn_code,
               quantity, selling_price, cost_price, fullfilment_type_name, fulfilment_team_name, service_type_name,
               billing_type_name, branch_po):
        self.log_in(username, password)
        self.sstf_visibilty()
        self.sstf_basic_info(sales_ex_name, sales_spe_name, prod_group_name, regularization_name)
        self.basic_details(branch_name, customer_name)
        self.sstf_calander()
        self.customer_names()
        self.add_address()
        self.add_docs(document=os.path.abspath("/Users/harshalijambhale/Documents/Book1.xlsx"))
        self.product(sbu_name, principal_name, product_name, hsn_code,
               quantity, selling_price, cost_price, fullfilment_type_name, fulfilment_team_name, service_type_name,
               billing_type_name)
        self.add_supplier_po_to_be_raised_from(branch_po)
        self.send_for_approval()

    def conditional_customer_po_stf(self, username, password, sales_ex_name, sales_spe_name, prod_group_name, regularization_name, branch_name, customer_name,  ):
        self.log_in(username, password)
        self.sstf_visibilty()
        self.sstf_basic_info(sales_ex_name, sales_spe_name, prod_group_name, regularization_name)
        branch = Select(self.driver.find_element(*self.branch_path))
        branch.select_by_visible_text(branch_name)
        customer_name_dd = Select(self.driver.find_element(*self.customer_name_path))
        customer_name_dd.select_by_index(customer_name)
        self.driver.find_element(*self.customer_po_path).send_keys(self.random_number_generator())











