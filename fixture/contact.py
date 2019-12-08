from selenium.webdriver.support.ui import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def addpage_opened(self):
        wd = self.app.wd # link for the browser driver
        wd.find_element_by_link_text("add new").click()

    def return_homepage(self):
        wd = self.app.wd # link for the browser driver
        wd.find_element_by_link_text("home").click()

    def add(self, contact):
        wd = self.app.wd # link for the browser driver
        self.addpage_opened()
        self.fill_all_fields(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_homepage()

    def fill_all_fields(self, contact):
        wd = self.app.wd # link for the browser driver
        self.fill_visiable_fields_on_homepage(contact)
        self.change_each_field("middlename", contact.middlename)
        self.change_each_field("company", contact.company)
        self.change_each_field("title", contact.title)
        self.change_each_field("homepage", contact.homepage)
        self.change_list_element("bday", contact.bday)
        self.change_list_element("bmonth", contact.bmonth)
        self.change_each_field("byear", contact.byear)
        self.change_list_element("aday", contact.bday)
        self.change_list_element("amonth", contact.bmonth)
        self.change_each_field("ayear", contact.ayear)
        self.change_each_field("address2", contact.address2)
        self.change_each_field("notes", contact.notes)

    def change_list_element(self, field_name, text):
        wd = self.app.wd
        Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def change_each_field(self, field_name, text):
        wd = self.app.wd # link for the browser driver
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first(self):
        wd = self.app.wd # link for the browser driver
        self.return_homepage()
        self.selected_first()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_homepage()

    def modify_first(self, contact):
        wd = self.app.wd # link for the browser driver
        self.return_homepage()
        self.selected_first()
        wd.find_element_by_xpath("(//img[@alt='Edit'])[2]").click()
        self.fill_visiable_fields_on_homepage(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_homepage()

    def fill_visiable_fields_on_homepage(self, contact):
        wd = self.app.wd # link for the browser driver
        self.change_each_field("firstname", contact.firstname)
        self.change_each_field("lastname", contact.lastname)
        self.change_each_field("address", contact.address)
        self.change_each_field("email", contact.email)
        self.change_each_field("email2", contact.email2)
        self.change_each_field("email3", contact.email3)
        self.change_each_field("home", contact.home)
        self.change_each_field("work", contact.work)
        self.change_each_field("mobile", contact.mobile)

    def selected_first(self):
        wd = self.app.wd # link for the browser driver
        wd.find_element_by_name("selected[]").click()