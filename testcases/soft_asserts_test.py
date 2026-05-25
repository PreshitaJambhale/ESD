import softest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class sstf_soft_asserts_test(softest.TestCase):
    pass
    '''

    sales_ex_path = (By.XPATH, "//select[@name='sstf[basic][iam_iss]']")

    def setUp(self):
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

    def test_sstf_basic_info(self):
        sales_ex = Select(self.driver.find_element(*self.sales_ex_path))

        expected_name = "John Doe"
        options = [opt.text.strip() for opt in sales_ex.options]

        self.soft_assert(
            self.assertIn,
            expected_name,
            options,
            "Dropdown option 'John Doe' not found inside Sales Executive dropdown")
        self.assert_all()




    def tearDown(self):
        self.driver.quit()
'''
