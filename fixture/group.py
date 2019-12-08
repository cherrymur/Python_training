class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd # link for the browser driver
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd # link for the browser driver
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        self.fill_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def change_each_field(self, field_name, text):
        wd = self.app.wd # link for the browser driver
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_form(self, group):
        wd = self.app.wd # link for the browser driver
        self.change_each_field("group_name", group.name)  # values defined in test_modify_group.py or test_create
        self.change_each_field("group_header", group.header)
        self.change_each_field("group_footer", group.footer)

    def return_to_groups_page(self):
        wd = self.app.wd # link for the browser driver
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

    def modify_first(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first()
        #open modification form
        wd.find_element_by_name("edit").click()
        self.fill_form(new_group_data) #was correct when I did myself
        #submit modification
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()


