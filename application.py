from selenium.webdriver.firefox.webdriver import WebDriver

class Application:
    def __init__(self):
        self.wd = WebDriver()#launch browser
        self.wd.implicitly_wait(60)

    def open_homepage(self):
        # open homepage
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def login(self, username, password):
        # login
        wd = self.wd
        self.open_homepage()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").submit()

    def open_groups_page(self):
        # open groups page
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def logout(self):
        # logout
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def create_group(self, group):
        # init groups creation
        wd = self.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        # return to group page
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def destroy(self):
        self.wd.quit()