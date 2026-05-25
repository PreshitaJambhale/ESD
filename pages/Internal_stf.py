import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import random
from datetime import date
import os

class InternalSTF():


    iss_path = (By.XPATH, "//select[@name = 'stf[basic][iam_iss]']")
    sales_specialist_path = (By.XPATH, "//select[@name = 'stf[basic][sales_specialist]']")
    tech_role_path = (By.XPATH, "//select[@name = 'stf[basic][tech_role]']")
    other_sales_path = (By.XPATH, "//select[@name = 'stf[basic][other_sales]']")
    stf_type_path = (By.XPATH, "//select[@name='stf[basic][stf_type]']")
    regularization_path = (By.XPATH, "//select[@name = 'stf[basic][is_regularization]']")

    branch_path = (By.XPATH, "//select[@name = 'stf[customer][branch]']")
    customer_name_path = (By.XPATH, "//select[@name = 'stf[customer][id]']")
    program_type_dropdown_path = (By.XPATH, "//select[@name='stf[basic][program_type]']")
    customer_po_input_path = (By.XPATH, "//input[@placeholder='Customer PO No']")
    customer_po_date_input_path = (By.XPATH, "//input[@name='stf[customer][date_po]']")
    purchase_type_pth = (By.XPATH, "//select[@name='stf[basic][purchase_type]']")

    po_month_dropdown_path = (By.XPATH, "/html/body/div[6]/div[1]/div/table/thead/tr[1]/th[2]/select[1]")
    po_year_dropdown_path = (By.XPATH, "/html/body/div[6]/div[1]/div/table/thead/tr[1]/th[2]/select[2]")
    po_date_select_path = (By.XPATH, "/html/body/div[6]/div[1]/div/table/tbody/tr[1]/td[4]")
    po_receive_date_input_path = (By.XPATH, "//input[@name='stf[customer][date_po_receive]']")
    receive_month_dropdown_path = (By.XPATH, "/html/body/div[7]/div[1]/div/table/thead/tr[1]/th[2]/select[1]")
    receive_year_dropdown_path = (By.XPATH, "/html/body/div[7]/div[1]/div/table/thead/tr[1]/th[2]/select[2]")
    receive_date_select_path = (By.XPATH, "/html/body/div[7]/div[1]/div/table/tbody/tr[1]/td[4]")

    product_sbu_dropdown_path = (By.XPATH, "//select[@name='stf[product][1][sbu_id]']")
    product_principal_dropdown_path = (By.XPATH, "//select[@name='stf[product][1][principal_id]']")
    product_name_input_path = (By.XPATH, "//input[@name='stf[product][1][name]']")
    product_search_query_input_path = (By.XPATH, "//input[@name='query']")
    product_search_button_path = (By.XPATH, "//button[normalize-space()='Search!']")
    product_select_first_result_path = (By.XPATH, "//*[@id='popup']/div[2]/div/div[2]/div[2]/table/tbody/tr[1]/td[1]/a")
    product_quantity_input_path = (By.XPATH, "//input[@name='stf[product][1][quantity]']")
    product_selling_price_input_path = (By.XPATH, "//input[@name='stf[product][1][selling_price]']")
    product_cost_price_input_path = (By.XPATH, "//input[@name='stf[product][1][cost_price]']")
    product_additional_collapse_arrow_path = (By.XPATH, "//div[@class='arrow additional-collapse cursor']")
    product_type_dropdown_path = (By.XPATH, "//select[@name='stf[product][1][is_discrete]']")
    product_billing_cycle_dropdown_path = (By.XPATH, "//select[@name='stf[product][1][billing_cycle]']")
    product_subscription_start_date_input_path = (By.XPATH, "//input[@name='stf[product][1][date_subscription_start]']")
    product_subscription_date_select_path = (By.XPATH, "/html/body/div[11]/div[1]/div/table/tbody/tr[5]/td[2]")
    product_subscription_period_input_path = (By.XPATH, "//input[@name='stf[product][1][subscription_period]']")
    product_order_type_dropdown_path = (By.XPATH, "//select[@name='stf[product][1][is_renewal]']")
    product_consumable_path = (By.XPATH, "(//select[@name = 'stf[product][1][category]'])[2]")


    product2_sbu_dropdown_path = (By.XPATH, "//select[@name='stf[product][2][sbu_id]']")
    product2_principal_dropdown_path = (By.XPATH, "//select[@name='stf[product][2][principal_id]']")
    product2_name_input_path = (By.XPATH, "//input[@name='stf[product][2][name]']")
    product2_quantity_input_path = (By.XPATH, "//input[@name='stf[product][2][quantity]']")
    product2_selling_price_input_path = (By.XPATH, "//input[@name='stf[product][2][selling_price]']")
    product2_cost_price_input_path = (By.XPATH, "//input[@name='stf[product][2][cost_price]']")
    product2_type_dropdown_path = (By.XPATH, "//select[@name='stf[product][2][is_discrete]']")
    product2_billing_cycle_dropdown_path = (By.XPATH, "//select[@name='stf[product][2][billing_cycle]']")
    product2_subscription_start_date_input_path = (By.XPATH, "//input[@name='stf[product][2][date_subscription_start]']")
    product2_subscription_date_select_path = (By.XPATH, "//body[1]/div[15]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[1]")
    product2_subscription_period_input_path = (By.XPATH, "//input[@name='stf[product][2][subscription_period]']")
    product2_order_type_dropdown_path = (By.XPATH, "//select[@name='stf[product][2][is_renewal]']")
    product2_isd_dropdown_path = (By.XPATH, "//select[@name='stf[product][2][isd_gst_type]']")
    product2_consumable_path = (By.XPATH, "(//select[@name = 'stf[product][2][category]'])[2]")
    product2_additional_collapse_arrow_path = (By.XPATH, "(//div[@class='arrow additional-collapse cursor'])")

    product3_sbu_dropdown_path = (By.XPATH, "//select[@name='stf[product][3][sbu_id]']")
    product3_principal_dropdown_path = (By.XPATH, "//select[@name='stf[product][3][principal_id]']")
    product3_name_input_path = (By.XPATH, "//input[@name='stf[product][3][name]']")
    product3_quantity_input_path = (By.XPATH, "//input[@name='stf[product][3][quantity]']")
    product3_selling_price_input_path = (By.XPATH, "//input[@name='stf[product][3][selling_price]']")
    product3_cost_price_input_path = (By.XPATH, "//input[@name='stf[product][3][cost_price]']")
    product3_type_dropdown_path = (By.XPATH, "//select[@name='stf[product][3][is_discrete]']")
    product3_order_type_dropdown_path = (By.XPATH, "//select[@name='stf[product][3][is_renewal]']")
    product3_isd_dropdown_path = (By.XPATH, "//select[@name='stf[product][3][isd_gst_type]']")
    product3_consumable_path = (By.XPATH, "(//select[@name = 'stf[product][3][category]'])[2]")
    product3_additional_collapse_arrow_path = (By.XPATH, "(//div[@class='arrow additional-collapse cursor'])")

    product4_sbu_dropdown_path = (By.XPATH, "//select[@name='stf[product][4][sbu_id]']")
    product4_principal_dropdown_path = (By.XPATH, "//select[@name='stf[product][4][principal_id]']")
    product4_name_input_path = (By.XPATH, "//input[@name='stf[product][4][name]']")
    product4_quantity_input_path = (By.XPATH, "//input[@name='stf[product][4][quantity]']")
    product4_selling_price_input_path = (By.XPATH, "//input[@name='stf[product][4][selling_price]']")
    product4_cost_price_input_path = (By.XPATH, "//input[@name='stf[product][4][cost_price]']")
    product4_type_dropdown_path = (By.XPATH, "//select[@name='stf[product][4][is_discrete]']")
    product4_order_type_dropdown_path = (By.XPATH,"//select[@name='stf[product][4][is_renewal]']")# FIXED (you had product[3])
    product4_isd_dropdown_path = (By.XPATH, "//select[@name='stf[product][4][isd_gst_type]']")
    product4_consumable_path = (By.XPATH, "(//select[@name = 'stf[product][4][category]'])[2]")
    product4_additional_collapse_arrow_path = (By.XPATH, "(//div[@class='arrow additional-collapse cursor'])")

    product5_sbu_dropdown_path = (By.XPATH, "//select[@name='stf[product][5][sbu_id]']")
    product5_principal_dropdown_path = (By.XPATH, "//select[@name='stf[product][5][principal_id]']")
    product5_name_input_path = (By.XPATH, "//input[@name='stf[product][5][name]']")
    product5_quantity_input_path = (By.XPATH, "//input[@name='stf[product][5][quantity]']")
    product5_selling_price_input_path = (By.XPATH, "//input[@name='stf[product][5][selling_price]']")
    product5_cost_price_input_path = (By.XPATH, "//input[@name='stf[product][5][cost_price]']")
    product5_type_dropdown_path = (By.XPATH, "//select[@name='stf[product][5][is_discrete]']")
    product5_order_type_dropdown_path = (By.XPATH, "//select[@name='stf[product][5][is_renewal]']")
    product5_isd_dropdown_path = (By.XPATH, "//select[@name='stf[product][5][isd_gst_type]']")
    product5_consumable_path = (By.XPATH, "(//select[@name = 'stf[product][5][category]'])[2]")
    product5_additional_collapse_arrow_path = (By.XPATH, "(//div[@class='arrow additional-collapse cursor'])")

    product6_sbu_dropdown_path = (By.XPATH, "//select[@name='stf[product][6][sbu_id]']")
    product6_principal_dropdown_path = (By.XPATH, "//select[@name='stf[product][6][principal_id]']")
    product6_name_input_path = (By.XPATH, "//input[@name='stf[product][6][name]']")
    product6_quantity_input_path = (By.XPATH, "//input[@name='stf[product][6][quantity]']")
    product6_selling_price_input_path = (By.XPATH, "//input[@name='stf[product][6][selling_price]']")
    product6_cost_price_input_path = (By.XPATH, "//input[@name='stf[product][6][cost_price]']")
    product6_type_dropdown_path = (By.XPATH, "//select[@name='stf[product][6][is_discrete]']")
    product6_isd_dropdown_path = (By.XPATH, "//select[@name='stf[product][6][isd_gst_type]']")
    product6_order_type_dropdown_path = (By.XPATH, "//select[@name='stf[product][6][is_renewal]']")
    product6_consumable_path = (By.XPATH, "(//select[@name = 'stf[product][6][category]'])[2]")
    product6_additional_collapse_arrow_path = (By.XPATH, "(//div[@class='arrow additional-collapse cursor'])")

    add_more_button_path = (By.XPATH, "(//button[@type='button'][normalize-space()='Add More'])[5]")

    po_raised_from_dropdown_path = (By.XPATH, "//select[@name='stf[customer][po_to_raised_from]']")
    send_for_approval_button_path = (By.XPATH, "//button[normalize-space()='Send for Approval']")

    stf_search_path = (By.XPATH, "//a[@href='/stf/search.html']//div[@class='service-icon']")
    first_stf_link_path = (By.XPATH,"//div[@class='form-group table-responsive col-md-12 col-sm-12 col-xs-12']/table/tbody/tr[1]/td/a")
    stf_id_path = (By.XPATH, "//div[@role='main']//div//div[1]//div[1]//div[2]//div[1]//div[1]//div[1]")


    def __init__(self,driver):
        self.driver = driver
        self.Wait = WebDriverWait(driver, 20)


    def customer_details(self):

        Select(self.driver.find_element(*self.iss_path)).select_by_visible_text("Chandra Shekar")
        Select(self.driver.find_element(*self.sales_specialist_path)).select_by_visible_text("Rahul Ursekar")
        Select(self.driver.find_element(*self.tech_role_path)).select_by_visible_text("Rini Shrivastava")
        Select(self.driver.find_element(*self.other_sales_path)).select_by_visible_text("Sai Gopal")

        Select(self.driver.find_element(*self.stf_type_path)).select_by_index(4)
        Select(self.driver.find_element(*self.regularization_path)).select_by_visible_text("No")

        # ================= CUSTOMER INFO =================

        Select(self.driver.find_element(*self.branch_path)).select_by_visible_text("Mumbai")
        Select(self.driver.find_element(*self.customer_name_path)).select_by_index(4)
        Select(self.driver.find_element(*self.purchase_type_pth)).select_by_index(2)



        import random
        random_number = random.randint(1000, 99999)
        self.driver.find_element(*self.customer_po_input_path).send_keys(
            f"automated-test-{random_number}"
        )

        # ================= PO DATE =================

        self.driver.find_element(*self.customer_po_date_input_path).click()
        Select(self.driver.find_element(*self.po_month_dropdown_path)).select_by_visible_text("Jan")
        Select(self.driver.find_element(*self.po_year_dropdown_path)).select_by_visible_text("2026")
        self.driver.find_element(*self.po_date_select_path).click()

        self.driver.find_element(*self.po_receive_date_input_path).click()
        Select(self.driver.find_element(*self.receive_month_dropdown_path)).select_by_visible_text("Jan")
        Select(self.driver.find_element(*self.receive_year_dropdown_path)).select_by_visible_text("2026")
        self.driver.find_element(*self.receive_date_select_path).click()



    def product1(self):
        Select(self.driver.find_element(*self.product_sbu_dropdown_path)).select_by_visible_text("Synergy")
        Select(self.driver.find_element(*self.product_principal_dropdown_path)).select_by_visible_text("ME-AD")

        self.Wait.until(EC.element_to_be_clickable(self.product_name_input_path)).click()

        self.Wait.until(EC.element_to_be_clickable(self.product_search_query_input_path)).send_keys(
            "One Time Implementation Cost"
        )
        self.driver.find_element(*self.product_search_button_path).click()
        self.Wait.until(EC.element_to_be_clickable(self.product_select_first_result_path)).click()

        self.driver.find_element(*self.product_quantity_input_path).send_keys("8")
        self.driver.find_element(*self.product_selling_price_input_path).send_keys("650000")
        self.driver.find_element(*self.product_cost_price_input_path).send_keys("560000")

        self.Wait.until(EC.element_to_be_clickable(self.product_additional_collapse_arrow_path)).click()
        Select(self.Wait.until(EC.visibility_of_element_located(self.product_type_dropdown_path))).select_by_visible_text("Subscription")
        Select(self.driver.find_element(*self.product_billing_cycle_dropdown_path)).select_by_visible_text("Monthly")
        self.driver.find_element(*self.product_subscription_start_date_input_path).click()
        self.driver.find_element(*self.product_subscription_date_select_path).click()
        self.driver.find_element(*self.product_subscription_period_input_path).send_keys(2)
        Select(self.driver.find_element(*self.product_consumable_path)).select_by_visible_text("Software charges")


    def product2(self):
        self.driver.find_element(*self.add_more_button_path).click()
        Select(self.driver.find_element(*self.product2_sbu_dropdown_path)).select_by_visible_text("C&A")
        Select(self.driver.find_element(*self.product2_principal_dropdown_path)).select_by_visible_text(
            "FORTINET")

        self.driver.find_element(*self.product2_name_input_path).click()

        self.Wait.until(EC.element_to_be_clickable(self.product_search_query_input_path)).send_keys(
            "24x7 FortiCare Contract"
        )
        self.driver.find_element(*self.product_search_button_path).click()
        self.Wait.until(EC.element_to_be_clickable(self.product_select_first_result_path)).click()

        self.driver.find_element(*self.product2_quantity_input_path).send_keys("10")
        self.driver.find_element(*self.product2_selling_price_input_path).send_keys("31000")
        self.Wait.until(EC.element_to_be_clickable(self.product2_cost_price_input_path)).send_keys("24000")
        self.Wait.until(EC.element_to_be_clickable(self.product2_additional_collapse_arrow_path)).click()
        Select(self.driver.find_element(*self.product2_type_dropdown_path)).select_by_visible_text("Subscription")
        Select(self.driver.find_element(*self.product2_billing_cycle_dropdown_path)).select_by_visible_text("Quarterly")
        self.driver.find_element(*self.product2_subscription_start_date_input_path).click()
        self.driver.find_element(*self.product2_subscription_date_select_path).click()
        self.driver.find_element(*self.product2_subscription_period_input_path).send_keys(12)
        Select(self.driver.find_element(*self.product2_isd_dropdown_path)).select_by_visible_text("GST")
        Select(self.driver.find_element(*self.product2_consumable_path)).select_by_visible_text("Software charges")

    def product3(self):
        self.driver.find_element(*self.add_more_button_path).click()
        Select(self.driver.find_element(*self.product3_sbu_dropdown_path)).select_by_visible_text("Apple")
        Select(self.driver.find_element(*self.product3_principal_dropdown_path)).select_by_visible_text(
            "Apple Accessories")

        self.driver.find_element(*self.product3_name_input_path).click()

        self.Wait.until(EC.element_to_be_clickable(self.product_search_query_input_path)).send_keys(
            "9.7 Inch iPad Tampered Glass"
        )
        self.driver.find_element(*self.product_search_button_path).click()
        self.Wait.until(EC.element_to_be_clickable(self.product_select_first_result_path)).click()

        self.driver.find_element(*self.product3_quantity_input_path).send_keys("16")
        self.driver.find_element(*self.product3_selling_price_input_path).send_keys("6500")
        self.Wait.until(EC.element_to_be_clickable(self.product3_cost_price_input_path)).send_keys("6000")

        self.Wait.until(EC.element_to_be_clickable(self.product3_additional_collapse_arrow_path)).click()
        Select(self.Wait.until(
            EC.visibility_of_element_located(self.product3_type_dropdown_path)
        )).select_by_visible_text("Discrete")
        #Select(self.driver.find_element(*self.product3_order_type_dropdown_path)).select_by_visible_text("Renewal")
        Select(self.driver.find_element(*self.product3_isd_dropdown_path)).select_by_visible_text("GST")
        Select(self.driver.find_element(*self.product3_consumable_path)).select_by_visible_text("Software charges")

    def product4(self):
        self.Wait.until(EC.visibility_of_element_located(self.add_more_button_path)).click()
        Select(self.driver.find_element(*self.product4_sbu_dropdown_path)).select_by_visible_text("Synergy")
        Select(self.driver.find_element(*self.product4_principal_dropdown_path)).select_by_visible_text(
            "ME-AD")

        self.driver.find_element(*self.product4_name_input_path).click()

        self.Wait.until(EC.element_to_be_clickable(self.product_search_query_input_path)).send_keys(
            "Softcell Implementation AD Audit Plus"
        )
        self.driver.find_element(*self.product_search_button_path).click()
        self.Wait.until(EC.element_to_be_clickable(self.product_select_first_result_path)).click()

        self.driver.find_element(*self.product4_quantity_input_path).send_keys("4")
        self.driver.find_element(*self.product4_selling_price_input_path).send_keys("410000")
        self.driver.find_element(*self.product4_cost_price_input_path).send_keys("380000")

        self.Wait.until(EC.element_to_be_clickable(self.product4_additional_collapse_arrow_path)).click()
        Select(self.Wait.until(EC.visibility_of_element_located(self.product4_type_dropdown_path))).select_by_visible_text("Non-Discrete")
        Select(self.driver.find_element(*self.product4_order_type_dropdown_path)).select_by_visible_text("Renewal")
        Select(self.driver.find_element(*self.product4_isd_dropdown_path)).select_by_visible_text("GST")
        Select(self.driver.find_element(*self.product4_consumable_path)).select_by_visible_text("Software charges")

    def product5(self):
        self.driver.find_element(*self.add_more_button_path).click()
        Select(self.driver.find_element(*self.product5_sbu_dropdown_path)).select_by_visible_text("Lateral")
        Select(self.driver.find_element(*self.product5_principal_dropdown_path)).select_by_visible_text(
            "DNS Hosting")

        self.driver.find_element(*self.product5_name_input_path).click()

        self.Wait.until(EC.element_to_be_clickable(self.product_search_query_input_path)).send_keys(
            "DNS Hosting Services"
        )
        self.driver.find_element(*self.product_search_button_path).click()
        self.Wait.until(EC.element_to_be_clickable(self.product_select_first_result_path)).click()

        self.driver.find_element(*self.product5_quantity_input_path).send_keys("20")
        self.driver.find_element(*self.product5_selling_price_input_path).send_keys("34200.96")
        self.driver.find_element(*self.product5_cost_price_input_path).send_keys("29840")

        self.Wait.until(EC.element_to_be_clickable(self.product5_additional_collapse_arrow_path)).click()
        Select(self.driver.find_element(*self.product5_type_dropdown_path)).select_by_visible_text("Non-Discrete")
        Select(self.driver.find_element(*self.product5_order_type_dropdown_path)).select_by_visible_text("Renewal")
        Select(self.driver.find_element(*self.product5_isd_dropdown_path)).select_by_visible_text("GST")
        Select(self.driver.find_element(*self.product5_consumable_path)).select_by_visible_text("Software charges")

    def product6(self):
        self.driver.find_element(*self.add_more_button_path).click()
        Select(self.driver.find_element(*self.product6_sbu_dropdown_path)).select_by_visible_text("Lateral")
        Select(self.driver.find_element(*self.product6_principal_dropdown_path)).select_by_visible_text(
            "Cloudflare")

        self.driver.find_element(*self.product6_name_input_path).click()

        self.Wait.until(EC.element_to_be_clickable(self.product_search_query_input_path)).send_keys(
            "Cloud flare"
        )
        self.driver.find_element(*self.product_search_button_path).click()
        self.Wait.until(EC.element_to_be_clickable(self.product_select_first_result_path)).click()

        self.driver.find_element(*self.product6_quantity_input_path).send_keys("1")
        self.driver.find_element(*self.product6_selling_price_input_path).send_keys("65000")
        self.driver.find_element(*self.product6_cost_price_input_path).send_keys("60000")

        self.driver.find_element(*self.product6_additional_collapse_arrow_path).click()

        Select(self.Wait.until(EC.visibility_of_element_located(self.product6_type_dropdown_path))).select_by_visible_text("Non-Discrete")
        Select(self.driver.find_element(*self.product6_order_type_dropdown_path)).select_by_visible_text("Renewal")
        Select(self.driver.find_element(*self.product6_isd_dropdown_path)).select_by_visible_text("GST")
        Select(self.driver.find_element(*self.product6_consumable_path)).select_by_visible_text("Software charges")

    def multiple_products(self):
        self.product1()
        self.product2()
        self.product3()
        self.product4()
        self.product5()
        self.product6()







