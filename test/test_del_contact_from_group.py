# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_del_contact_from_group(app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="training", header="training", footer="training"))
    group_list = db.get_group_list()
    random_group = random.choice(group_list)
    group_id = random_group.id
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Avramenko", middlename="Olga", lastname="shdjs", nickname="cherrymur",
                                   title="dshdj", company="hjhj", address="hjhj", homephone="hj", mobilephone="hjh", workphone="hjh",
                                   faxphone="hjhj",
                                   email="ghgh", email2="hgh", email3="hgh", homepage="hghg", bday="31",
                                   bmonth="December", byear="1990",
                                   aday="12", amonth="October", ayear="1236", address2="dsfef", secondaryphone="sas",
                                   notes="dsd"))
        new_contact = db.get_contact_list()[0]
        app.contact.add_contact_in_group_by_id(new_contact.id, group_id)
    elif len(db.get_contacts_in_group(Group(id="%s" % group_id))) == 0:
        contact_list_not_in_group = db.get_contacts_not_in_group(Group(id="%s" % group_id))
        random_contact = random.choice(contact_list_not_in_group)
        app.contact.add_contact_in_group_by_id(random_contact.id, group_id)
    old_contacts_in_group = db.get_contacts_in_group(Group(id="%s" % group_id))
    old_contacts_list = db.get_contact_list()
    random_contact = random.choice(old_contacts_in_group)
    app.contact.del_contact_from_group_by_id(random_contact.id, group_id)
    new_contacts_list = db.get_contact_list()
    new_contacts_in_group = db.get_contacts_in_group(Group(id="%s" % group_id))
    old_contacts_in_group.remove(random_contact)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)