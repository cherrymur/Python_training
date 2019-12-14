# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_list()
    added_contact = Contact(firstname="Avramenko", middlename="Olga", lastname="shdjs", nickname="cherrymur",
                            title="dshdj", company="hjhj", address="hjhj", home="hj", mobile="hjh", work="hjh",
                            fax="hjhj",
                            email="ghgh", email2="hgh", email3="hgh", homepage="hghg", bday="31", bmonth="December",
                            byear="1990",
                            aday="12", amonth="October", ayear="1236", address2="dsfef", phone2="sas", notes="dsd")
    app.contact.create(added_contact)
    new_contacts = app.contact.get_list()
    assert (len(old_contacts) + 1) == len(new_contacts)
    old_contacts.append(added_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
