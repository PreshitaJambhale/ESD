
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from utilities import utils_for_stf

class EsdUpload():

    search_button = (By.XPATH, "//button[@value='Search']")
    PO_number = (By.XPATH, "//input[@placeholder='PO. No.']")
    checkbox = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/form[2]/table[1]/thead[1]/tr[1]/th[1]/label[1]/div[1]")
    upload1 = (By.XPATH, "//button[@name='attachment']")
    document_for = (By.XPATH, "//select[@class='pre-loaded apply-to-all-use select2-hidden-accessible']")
    upload2 = (By.XPATH, "//button[normalize-space()='Upload']")

    document_to_all =  (By.XPATH, "//button[@class='btn btn-success apply-to-all-use']")
    date_to_all = (By.XPATH, "//button[@class='btn btn-danger apply-to-all-license']")

    l_start_date = (By.XPATH, "//input[@placeholder='Start date']")
    date1 = (By.CSS_SELECTOR, "body > div:nth-child(9) > div:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(6)")

    l_end_date = (By.XPATH, "//input[@placeholder='End date']")
    date2 = (By.CSS_SELECTOR, "body > div:nth-child(10) > div:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(4) > td:nth-child(4)")

    save = (By.XPATH, "//button[@name='save']")

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def search_and_upload(self, PO_number):
        po =self.wait.until(EC.element_to_be_clickable((self.PO_number)))
        po.send_keys(PO_number)
        self.wait.until(EC.element_to_be_clickable(self.search_button)).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.upload1).click()
        self.driver.find_element(*self.upload2).click()

    def apply_to_all(self, type):
        ut = utils_for_stf.Utils(self.driver)
        ut.handle_drop_down((self.document_for), type)
        self.driver.find_element(*self.document_to_all).click()
        ut.handle_calendar((self.l_start_date), (self.date1))
        ut.handle_calendar((self.l_end_date), (self.date2))
        self.driver.find_element(*self.date_to_all).click()
        self.wait.until(EC.visibility_of_element_located(self.save)).click()




