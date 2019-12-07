from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:
    def __init__(self):
        self.wd = WebDriver()#launch browser
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self) #allow to use wd in session.py
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:# check any problems
            return False

    def open_homepage(self):
        # open homepage
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()