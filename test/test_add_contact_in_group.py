# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact_in_group(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list_in_group()
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui: # flag to on/off assert
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_list(), key=Contact.id_or_max)