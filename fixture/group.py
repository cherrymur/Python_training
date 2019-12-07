class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        self.fill_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def fill_each_field(self, text, group):
        wd = self.app.wd
        wd.find_element_by_name(text).click()
        wd.find_element_by_name(text).clear()
        wd.find_element_by_name(text).send_keys(group)

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def delete_first(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def select_first(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first()
        wd.find_element_by_name("edit").click()
        self.fill_form(group)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def fill_form(self, group):
        self.fill_each_field("group_name", group.name)  # values defined in test_modify_group.py or test_create
        self.fill_each_field("group_header", group.header)
        self.fill_each_field("group_footer", group.footer)

