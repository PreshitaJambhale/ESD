from datetime import date

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Utils:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def get_current_date(self):
        today = date.today()
        current_date = today.day
        return current_date

    def handle_click(self,locator):
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except ValueError:
            print("Invalid conversion")
        except Exception:
            print("Some other error")

    def handle_send_keys(self,locator, value):
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).send_keys(value)
        except ValueError:
            print("Invalid conversion")
        except Exception:
            print("Some other error")

    def handle_drop_down(self, locator, value):
        try:
            locator_type = Select(self.driver.find_element(*locator))
            locator_type.select_by_visible_text(value)
        except ValueError:
            print("Invalid conversion")
        except Exception:
            print("Some other error")

    def handle_calendar(self, cal_loc, date_loc):
        self.driver.find_element(*cal_loc).click()
        self.driver.find_element(*date_loc).click()

