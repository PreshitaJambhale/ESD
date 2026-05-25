

from configparser import ConfigParser

from configparser import ConfigParser
import os

config = ConfigParser()

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config_path = os.path.join(base_dir, "configfiles", "config.ini")

config.read(config_path)


class ReadConfigfiles:

    @staticmethod
    def get_esd_upload():
        print(config.sections())
        return config.get("environment", "esd_upload_url")

    @staticmethod
    def get_esd_update():
        return config.get("environment", "esd_update_url")

    @staticmethod
    def get_browser():
        return config.get("environment", "browser")

    @staticmethod
    def get_PE_username():
        return config.get("environment", "pe_username")

    @staticmethod
    def get_username():
        return config.get("environment", "username")

    @staticmethod
    def get_password():
        return config.get("environment", "password")

    @staticmethod
    def get_esd_attach():
        return config.get("environment", "esd_attachment_url")

    @staticmethod
    def get_esd_search():
        return config.get("environment", "esd_search_url")





