


import pytest



from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    Wait = WebDriverWait(driver, 20)
    driver.get("https://ops2uat2.softcell.in/")
    request.cls.driver = driver
    request.cls.Wait = Wait
    driver.maximize_window()
    yield
    driver.quit()