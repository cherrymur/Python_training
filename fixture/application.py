from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:
    def __init__(self):
        self.wd = WebDriver()  # initialize wd variable
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)  # link to SessionHelper
        self.group = GroupHelper(self) # link to GroupHelper
        self.contact = ContactHelper(self) # link to ContactHelper

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:# check any problems
            return False

    def open_homepage(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
