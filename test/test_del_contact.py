from model.contact import Contact
from random import randrange


def test_del_first_contact(app):
    # check that one or more contact exist
    if app.contact.count_c() == 0:
        app.contact.create(Contact(firstname="Avramenko", middlename="Olga", lastname="shdjs", nickname="cherrymur",
                                   title="dshdj", company="hjhj", address="hjhj", home="hj", mobile="hjh", work="hjh",
                                   fax="hjhj",
                                   email="ghgh", email2="hgh", email3="hgh", homepage="hghg", bday="31",
                                   bmonth="December", byear="1990",
                                   aday="12", amonth="October", ayear="1236", address2="dsfef", phone2="sas",
                                   notes="dsd"))
    old_contacts = app.contact.get_list()
    index = randrange(len(old_contacts))
    app.contact.delete_by_index(index)
    assert len(old_contacts) == app.contact.count_c()
    new_contacts = app.contact.get_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
