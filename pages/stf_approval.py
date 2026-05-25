import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class StfApproval():
    stf_icon_path = (By.XPATH, "//a[@href='/stf/']")
    stf_search_path = (By.XPATH, "//a[@href='/stf/search.html']//div[@class='service-icon']")
    user_dropdown_icon_path = (By.XPATH, "//i[@class='fa fa-arrow-down']")
    logout_button_path = (By.XPATH, "//a[normalize-space()='Log Out']")
    username_input_path = (By.XPATH, "//input[@id='username']")
    password_input_path = (By.XPATH, "//input[@id='password']")
    login_button_path = (By.XPATH, "//button[normalize-space()='Log in']")
    first_stf_link_path = (By.XPATH, "//div[@class='form-group table-responsive col-md-12 col-sm-12 col-xs-12']/table/tbody/tr[1]/td/a")
    interstate_purchase_radio_path = (By.XPATH,"//label[@class='control control--radio'][normalize-space()='Inter-state']//div[@class='control__indicator']")
    purchase_igst_input_path = (By.XPATH, "//input[@name='purchase[igst]']")
    interstate_billing_radio_path = (By.XPATH, "//label[@class='control control--radio interStateMargin']//div[@class='control__indicator']")
    normal_customer_radio_path = (By.XPATH, "//label[normalize-space()='Normal']//div[@class='control__indicator']" )
    billing_igst_input_path = (By.XPATH, "//input[@name='billing[igst]']")
    approve_button_path = (By.XPATH, "//button[normalize-space()='Approve']")
    stf_number_cell_path = (By.XPATH,"//div[@class='form-group table-responsive col-md-12 col-sm-12 col-xs-12']/table/tbody/tr[1]/td[1]")
    supplier_po_sidebar_path = (By.XPATH, "//a[normalize-space()='Supplier PO']")
    create_po_link_path = (By.XPATH, "//a[@href='/po/create-po.html']")
    stf_search_input_path = (By.XPATH, "//input[@placeholder='STF/SSTF No.']")
    stf_search_button_path = (By.XPATH, "//input[@value='Search']")
    select_all_checkbox_path = (By.XPATH, "//tr[@class='headings']//div[@class='control__indicator']")
    create_po_button_path = (By.XPATH, "//button[@class='btn btn-primary source raise-po']")
    supplier_name_dropdown_path = (By.XPATH, "//select[@name='po[supplier][id]']")
    supplier_attention_dropdown_path = (By.XPATH, "//select[@name='po[supplier_contacts][id]']")
    print_customer_details_no_radio_path = (By.XPATH,"//div[@class='apply-to-all']//label[@class='control control--radio'][normalize-space()='No']")
    expected_delivery_date_field_path = (By.XPATH,"//*[@id='demo-form2']/div/div[5]/div/div/div[2]/div[2]/div[2]")
    expected_delivery_date_select_path = (By.XPATH,"/html/body/div[9]/div[1]/div/table/tbody/tr[3]/td[6]")
    apply_to_all_date_checkbox_path = (By.XPATH, "//input[@name='apply-to-all']")
    select_items_checkbox_path = (By.XPATH, "//tr[@class='heading']//div[@class='control__indicator']")
    igst_value_input_path = (By.XPATH, "//input[@value='17']")
    apply_tax_button_path = (By.XPATH, "//button[normalize-space()='Apply Tax Details']")
    billing_location_dropdown_path = (By.XPATH, "//select[@name='po[delivery][billing_location]']")
    shipping_location_dropdown_path = (By.XPATH, "//select[@name='po[delivery][shipping_location]']")
    shipping_type_dropdown_path = (By.XPATH, "//select[@name='po[delivery][shipping_type]']")
    credit_days_input_path = (By.XPATH, "//input[@placeholder='Credit days by supplier']")
    payment_terms_textarea_path = (By.XPATH, "//textarea[@placeholder='Enter playment terms associated with supplier']")
    submit_po_for_approval_button_path = (By.XPATH, "//button[normalize-space()='Submit PO for Approval']")
    po_pending_for_approval_row_path = (By.XPATH,"/html/body/div[2]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/form/div[2]/form/div[1]/table/tbody/tr[1]/td[1]")

    final_po_approve_button_path = (By.XPATH, "//button[@name='po']")

    def __init__(self,driver):
        self.driver = driver
        self.Wait = WebDriverWait(driver, 20)


    def stf_visibilty(self):

        self.driver.find_element(*self.stf_icon_path).click()
        self.driver.find_element(*self.stf_search_path).click()
        time.sleep(5)
        self.driver.find_element(*self.first_stf_link_path).click()

    def handles_windows(self):
        windows = self.driver.window_handles
        parent_window = self.driver.current_window_handle()
        element = self.driver.find_element(*self.first_stf_link_path)
        element.click()
        child_window = self.driver.current_window_handle()
        print(windows)
        handles = self.driver.window_handles
        for i in handles:
            print(i.title())
        self.driver.switch_to.window(handles[1])


    def stf_approval(self):
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0,1000)")

        self.driver.find_element(*self.interstate_purchase_radio_path).click()

        self.driver.find_element(*self.purchase_igst_input_path).send_keys("18")

        self.driver.find_element(*self.interstate_billing_radio_path).click()
        self.driver.find_element(*self.normal_customer_radio_path).click()

        self.driver.find_element(*self.billing_igst_input_path).send_keys("18")

        self.driver.find_element(*self.approve_button_path).click()

