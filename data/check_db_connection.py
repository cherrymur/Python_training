from fixture.orm import ORMFixture # DbFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_contact_list() # get_contact_list()
    for item in l:
        print(item)
    print(len(l))
finally:
    pass
    # db.destroy()