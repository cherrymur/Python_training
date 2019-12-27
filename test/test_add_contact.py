# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata =[
    Contact(firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname, title=title,
            company=company, address=address, homephone=homephone, mobilephone=mobilephone, workphone=workphone,
            faxphone=faxphone, email=email, email2=email2, email3=email3, homepage=homepage, address2=address2,
            secondaryphone=secondaryphone, notes=notes)
    for firstname in ["", random_string("firstname", 10)]
    for middlename in ["", random_string("middlename", 10)]
    for lastname in ["", random_string("lastname", 20)]
    for nickname in ["", random_string("nickname", 20)]
    for title in ["", random_string("title", 20)]
    for company in ["", random_string("company", 20)]
    for address in ["", random_string("address", 20)]
    for homephone in ["", random_string("homephone", 20)]
    for mobilephone in ["", random_string("mobilephone", 20)]
    for workphone in ["", random_string("workphone", 20)]
    for faxphone in ["", random_string("faxphone", 20)]
    for email in ["", random_string("email", 20)]
    for email2 in ["", random_string("email2", 20)]
    for email3 in ["", random_string("email3", 20)]
    for homepage in ["", random_string("homepage", 20)]
    for secondaryphone in ["", random_string("secondaryphone", 20)]
    for address2 in ["", random_string("address2", 20)]
    for notes in ["", random_string("notes", 20)]
]

#testdata =[Group(name="", header="", footer="")] + [
 #   Group(name=random_string("name", 10), header=random_string("header", 10), footer=random_string("footer", 10))
  #  for i in range(5)
#]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_list()
    app.contact.create(contact)
    assert (len(old_contacts) + 1) == app.contact.count_c()
    new_contacts = app.contact.get_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
