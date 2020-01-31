from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def opened_add_new_page(self):
        wd = self.app.wd  # link for the browser driver
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd  # link for the browser driver
        # wd.find_element_by_link_text("add new").click()  # for checking if in opened_add_new_page
        self.opened_add_new_page()
        self.fill_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        wd.find_element_by_css_selector("div.msgbox")
        self.return_homepage()
        self.contact_cache = None

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
        self.change_each_field("firstname", contact.firstname)
        self.change_each_field("lastname", contact.lastname)
        self.change_each_field("address", contact.address)
        self.change_each_field("email", contact.email)
        self.change_each_field("email2", contact.email2)
        self.change_each_field("email3", contact.email3)
        self.change_each_field("home", contact.homephone)
        self.change_each_field("work", contact.workphone)
        self.change_each_field("mobile", contact.mobilephone)
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
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.find_element_by_xpath("//li/a").click()

    def delete_first(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd  # link for the browser driver
        self.return_homepage()
        self.select_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox") # fix test_del_contact fail result
        self.return_homepage()
        self.contact_cache = None

    def delete_by_id(self, id):
        wd = self.app.wd  # link for the browser driver
        self.return_homepage()
        self.select_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox") # fix test_del_contact fail result
        self.return_homepage()
        self.contact_cache = None

    def select_first(self):
        self.select_by_index(0)

    def select_by_index(self, index):
        wd = self.app.wd  # link for the browser driver
        wd.find_elements_by_name("selected[]")[index].click()

    def select_by_id(self, id):
        wd = self.app.wd  # link for the browser driver
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def modify_first(self, new_contact_data):
        self.modify_by_index(0, new_contact_data)

    def modify_by_index(self, index, new_contact_data):
        wd = self.app.wd  # link for the browser driver
        self.return_homepage()

        # open modification form
        self.select_to_edit_by_index(index)
        self.fill_form(new_contact_data)

        # submit
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_homepage()
        self.contact_cache = None

    def modify_by_id(self, id, new_contact_data):
        wd = self.app.wd  # link for the browser driver
        self.return_homepage()

        # open modification form
        self.select_to_edit_by_id(id)
        self.fill_form(new_contact_data)

        # submit
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_homepage()
        self.contact_cache = None

    def select_to_edit_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("(//img[@alt='Edit'])")[index].click()

    def select_to_edit_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % id).click()

    def select_to_edit_first(self):
        self.edit_by_index(0)

    def count_c(self):
        wd = self.app.wd
        self.return_homepage()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_homepage()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                graphs = element.find_elements_by_tag_name("td")
                firstname = graphs[2].text
                lastname = graphs[1].text
                id = graphs[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = graphs[5].text
                all_emails = graphs[4].text
                address = graphs[3].text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails, address=address))
        return list(self.contact_cache)

    def open_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_homepage()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_info_from_edit_page(self, index):
        wd = self.app.wd
        self.select_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone, email=email, email2=email2,
                       email3=email3, address=address)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_view_by_index(index)
        text = wd.find_element_by_id("content").text
        if re.search("H: (.*)", text) is not None:
            homephone = re.search("H: (.*)", text).group(1)
        if re.search("W: (.*)", text) is not None:
            workphone = re.search("W: (.*)", text).group(1)
        if re.search("M: (.*)", text) is not None:
            mobilephone = re.search("M: (.*)", text).group(1)
        if re.search("P: (.*)", text) is not None:
            secondaryphone = re.search("P: (.*)", text).group(1)
        all_emails = re.findall("(.*)@(.*).(.*)", text)
        all_emails = "\n".join(list(all_emails))
        self.return_homepage()
        return Contact(id=id, homephone=homephone, workphone=workphone, mobilephone=mobilephone,
                       secondaryphone=secondaryphone, all_emails_from_view_page=all_emails)

    def add_contact_in_group_by_id(self, id, group_id):
        wd = self.app.wd
        self.return_homepage()
        self.select_by_id(id)
        wd.find_element_by_name("to_group").click()
        Select(wd.find_element_by_name("to_group"))
        wd.find_element_by_xpath("(//option[@value='%s'])[2]" % group_id).click()
        wd.find_element_by_name("add").click()
        #wd.find_element_by_xpath("//a[contains(@href, './?group=%s')]" % group_id).click()

    def del_contact_from_group_by_id(self, id, group_id):
        wd = self.app.wd
        self.open_group_page(group_id)
        self.select_by_id(id)
        wd.find_element_by_name("remove").click()
        # wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")  # fix test_del_contact fail result
        self.return_homepage()
        self.contact_cache = None

    def open_group_page(self, group_id):
        wd = self.app.wd  # link for the browser driver
        if not (wd.current_url.endswith("addressbook/?group=%s" % group_id)):
            wd.get("http://localhost/addressbook/?group=%s" % group_id)

''' another way to  write     select_to_edit_by_index
def open_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_homepage()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click() '''

