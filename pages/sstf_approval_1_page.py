
import time


from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class test_approval_1():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def test3(self):
        time.sleep(2)
        self.Wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@href='/sstf/search.html']//div[@class='service-icon']"))).click()
        self.Wait.until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[2]/div/div[3]/div[3]/div/div/div/div[2]/table/tbody/tr[1]/td[1]/a"))).click()
        handles = self.driver.window_handles
        for i in handles:
            print(i.title())
        self.driver.switch_to.window(handles[1])
        self.Wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='user-profile dropdown-toggle']//i[@class='fa fa-briefcase']"))).click()
        self.Wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Log Out']"))).click()
        self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys("Shivjirb")
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Test")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Log in']").click()
        time.sleep(4)
        '''
        checkboxes = self.driver.find_elements(By.XPATH, "//table[@class='table table-striped']//input[@type='checkbox']")
        print(f"{checkboxes} &  {len(checkboxes)}")
        for i in checkboxes:
            i.click()
            time.sleep(0.5)

        risk_involved = Select(self.driver.find_element(By.XPATH, "//select[@name = 'verdict[basic][risk]']"))
        risk_involved.select_by_visible_text('No')

        '''
        remark = self.driver.find_element(By.XPATH, "//textarea[@name='verdict[basic][remark]']")
        remark.send_keys("approved by shrikant")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Approve']").click()
        time.sleep(5)

        """ """
        # self.driver.switch_to.window(handles[0])

        self.driver.find_element(By.XPATH,
                                 "//a[@class='user-profile dropdown-toggle']//i[@class='fa fa-briefcase']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Log Out']").click()
        self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys("deepakf")
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Test")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Log in']").click()
        time.sleep(10)
        # self.Wait.until(EC.element_to_be_clickable(
        # (By.XPATH, "/html/body/div[2]/div/div[3]/div[3]/div/div/div/div[2]/table/tbody/tr[1]/td[1]/a"))).click()
        text = self.driver.find_element(By.XPATH,
                                        "/html/body/div[2]/div/div[3]/div[11]/div/div/div[2]/div/div/table/tbody/tr[2]/td[3]").text
        assert text == "SSTF has been approved by SI-SECNTL with risk"
        # self.driver.switch_to.window(handles[2])
        self.driver.find_element(By.XPATH, "//textarea[@name = 'verdict[basic][remark]']").send_keys(
            "approved by deepak")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Approve']").click()

        self.driver.quit()

        time.sleep(5)
        self.driver.switch_to.window(handles[1])
        self.driver.find_element(By.XPATH, "//a[@class='user-profile dropdown-toggle']//i[@class='fa fa-briefcase']").click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Log Out']").click()
        if Branch == "Mumbai":
            branch_commercial = "Gsurve"
        elif Branch == "Delhi":
            branch_commercial = "Kmishra"
        elif Branch == "Pune":
            branch_commercial = "aditi"
        elif Branch == "Bangalore" or Branch == "Hyderabad":
            branch_commercial = "sampathb"
        else:
            branch_commercial = "gsurve"

        self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys(branch_commercial)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Test")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Log in']").click()
        time.sleep(2)
        self.driver.switch_to.window(handles[1])
        risk_involved = Select(self.driver.find_element(By.XPATH, "//select[@name = 'verdict[basic][risk]']"))
        risk_involved.select_by_visible_text('No')
        self.driver.find_element(By.XPATH, "//textarea[@name = 'verdict[basic][remark]']").send_keys("Approved by BC")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Approve']").click()


         time.sleep(2)
         self.driver.find_element(By.XPATH, "//a[@class='user-profile dropdown-toggle']//i[@class='fa fa-briefcase']").click()
         self.driver.find_element(By.XPATH, "//a[normalize-space()='Log Out']").click()
         self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys("spat")
         self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Test")
         self.driver.find_element(By.XPATH, "//button[normalize-space()='Log in']").click()
         self.driver.switch_to.window(handles[1])
         self.driver.find_element(By.XPATH, "//textarea[@name = 'verdict[basic][remark]']").send_keys("approved by S. Patanakar")
         self.driver.find_element(By.XPATH, "//button[normalize-space()='Approve']").click()
