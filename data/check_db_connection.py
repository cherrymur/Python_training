from fixture.orm import ORMFixture # DbFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_contact_list()  # get_contacts_not_in_group(Group(id="82"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass
    # db.destroy()