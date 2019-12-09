from selenium.webdriver.support.ui import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def opened_add_new_page(self):
        wd = self.app.wd  # link for the browser driver
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd  # link for the browser driver
        self.opened_add_new_page()
        self.fill_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_homepage()

    def change_each_field(self, field_name, text):
        wd = self.app.wd  # link for the browser driver
        if text is not None:
            try:
                wd.find_element_by_name(field_name).click()
                wd.find_element_by_name(field_name).clear()
                wd.find_element_by_name(field_name).send_keys(text)
            except:
                Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def fill_form(self, contact):
        wd = self.app.wd  # link for the browser driver
        self.change_each_field("firstname", contact.firstname)
        self.change_each_field("lastname", contact.lastname)
        self.change_each_field("address", contact.address)
        self.change_each_field("email", contact.email)
        self.change_each_field("email2", contact.email2)
        self.change_each_field("email3", contact.email3)
        self.change_each_field("home", contact.home)
        self.change_each_field("work", contact.work)
        self.change_each_field("mobile", contact.mobile)
        self.change_each_field("middlename", contact.middlename)
        self.change_each_field("company", contact.company)
        self.change_each_field("title", contact.title)
        self.change_each_field("homepage", contact.homepage)
        self.change_each_field("bday", contact.bday)
        self.change_each_field("bmonth", contact.bmonth)
        self.change_each_field("byear", contact.byear)
        self.change_each_field("aday", contact.aday)
        self.change_each_field("amonth", contact.amonth)
        self.change_each_field("ayear", contact.ayear)
        self.change_each_field("address2", contact.address2)
        self.change_each_field("notes", contact.notes)

    def return_homepage(self):
        wd = self.app.wd  # link for the browser driver
        wd.find_element_by_xpath("//li/a").click()

    def delete_first(self):
        wd = self.app.wd  # link for the browser driver
        self.return_homepage()
        self.select_first()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_homepage()

    def select_first(self):
        wd = self.app.wd  # link for the browser driver
        wd.find_element_by_name("selected[]").click()

    def modify_first(self, new_contact_data):
        wd = self.app.wd  # link for the browser driver
        self.return_homepage()
        self.select_first()

        # open modification form
        wd.find_element_by_xpath("(//img[@alt='Edit'])").click()
        self.fill_form(new_contact_data)

        # submit
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_homepage()

    def count(self):
        wd = self.app.wd
        self.return_homepage()
        return len(wd.find_elements_by_name("selected[]"))