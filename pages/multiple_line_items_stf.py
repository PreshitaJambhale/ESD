import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import random
from datetime import date
import os

class MultipleLineItems():

    def __init__(self,driver):
        self.driver = driver
        self.Wait = WebDriverWait(driver, 20)

    # ---------------- LOGIN ---------------- #


    def multiple_line_items(self, products):

        for i in range(1, products + 1):

            Select(self.Wait.until(EC.element_to_be_clickable((By.NAME, f"stf[product][{i}][sbu_id]")))).select_by_visible_text("C&A")

            Select(self.Wait.until(EC.element_to_be_clickable((By.NAME, f"stf[product][{i}][principal_id]")))).select_by_visible_text("Nutanix")

            self.Wait.until(EC.element_to_be_clickable((By.NAME, f"stf[product][{i}][name]"))).click()

            self.Wait.until(EC.element_to_be_clickable((By.NAME, "query"))).send_keys("12 x 32GB (384GB per node)")

            self.Wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Search!']"))).click()

            self.Wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='popup']//table/tbody/tr[1]/td[1]/a"))).click()

            self.Wait.until(EC.element_to_be_clickable((By.NAME, f"stf[product][{i}][quantity]"))).send_keys("10")

            self.Wait.until(EC.element_to_be_clickable((By.NAME, f"stf[product][{i}][selling_price]"))).send_keys("5000")

            self.Wait.until(EC.element_to_be_clickable((By.NAME, f"stf[product][{i}][cost_price]"))
            ).send_keys("4450")

            self.driver.find_element(By.XPATH, "//div[@class='arrow additional-collapse cursor']").click()

            Select(self.Wait.until(EC.element_to_be_clickable(
                (By.NAME, f"stf[product][{i}][is_discrete]"))
            )).select_by_visible_text("Non-Discrete")

            Select(self.Wait.until(EC.element_to_be_clickable(
                (By.NAME, f"stf[product][{i}][is_renewal]"))
            )).select_by_visible_text("Renewal")

            Select(self.Wait.until(EC.element_to_be_clickable(
                (By.NAME, f"stf[product][{i}][isd_gst_type]"))
            )).select_by_visible_text("GST")

            if i< products:
                self.driver.find_element(By.XPATH, "(//button[@type='button'][normalize-space()='Add More'])[5]").click()

