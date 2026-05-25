import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



class BaseDriver:

    login_path = (By.XPATH, "//input[@id='username']")
    password_path = (By.XPATH, "//input[@id='password']")
    admit_path = (By.XPATH, "//button[normalize-space()='Log in']")
    logout_toggle = (By.XPATH, "//a[@class='user-profile dropdown-toggle']//i[@class='fa fa-briefcase']")
    logout_path = (By.XPATH, "//a[normalize-space()='Log Out']")

    def __init__(self, driver):
        self.driver = driver
        self.Wait = WebDriverWait(driver, 10)

    def open_url(self, url):
        self.driver.get(url)


    def login(self, username, password):
        self.driver.find_element(*self.login_path).send_keys(username)
        self.driver.find_element(*self.password_path).send_keys(password)
        self.driver.find_element(*self.admit_path).click()

    def log_out(self):
        self.driver.find_element(*self.logout_toggle).click()
        self.driver.find_element(*self.logout_path).click()

    def handle_control(self, handle_number):
        handles = self.driver.window_handles
        for i in handles:
            print(i.title())
        self.driver.switch_to.window(handles[handle_number])


