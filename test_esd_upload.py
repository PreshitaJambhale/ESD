import time
import pytest
from base.Base_file1 import BaseDriver
from pages.esd_upload_page import EsdUpload
from utilities.read_config import ReadConfigfiles


@pytest.mark.usefixtures("setup")
class Test_EsdUpload():

    def test_esd_upload(self):
        bd = BaseDriver(self.driver)
        ed = EsdUpload(self.driver)
        bd.open_url(ReadConfigfiles.get_esd_upload())
        bd.login(ReadConfigfiles.get_username(), ReadConfigfiles.get_password())
        ed.search_and_upload("STG-PO-2027-0065")
        time.sleep(2)
        current_url = self.driver.current_url
        assert current_url == ReadConfigfiles.get_esd_attach(), "Attachment page does not open."

        ed.apply_to_all("Both (Internal & Customer)")
        time.sleep(2)
        current_url = self.driver.current_url
        assert current_url == ReadConfigfiles.get_esd_search(), "Document did not get uploaded."









