from fixture.orm import ORMFixture # DbFixture
from model.group import Group
import random

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    group_list = db.get_group_list()
    random_group = random.choice(group_list)
    group_id = random_group.id
    l = db.get_contacts_in_group(Group(id="%s" % group_id))  # get_contacts_in_group(Group(id="82"))  # get_contact_list()
    for item in l:
        print(item)
    print(len(l))
finally:
    pass
    # db.destroy()