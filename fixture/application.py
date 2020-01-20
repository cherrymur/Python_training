from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:
    def __init__(self, browser, baseUrl):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("unknown %s" % browser)
        # initialize wd variable
        self.wd.implicitly_wait(5)  # not delete because tests are failed
        self.session = SessionHelper(self)  # link to SessionHelper
        self.group = GroupHelper(self)  # link to GroupHelper
        self.contact = ContactHelper(self)  # link to ContactHelper
        self.baseUrl = baseUrl

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
        except:  # check any problems
            return False

    def open_homepage(self):
        wd = self.wd
        wd.get(self.baseUrl)

    def destroy(self):
        self.wd.quit()
