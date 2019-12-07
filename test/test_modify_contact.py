# -*- coding: utf-8 -*-
from model.contact import Contact

def test_mod_firstname(app):
    app.session.login(username="admin",
                   password="secret")  # don't change because these fields will not changed(almost 100% only 2 parametrs)
    app.contact.modify_first(Contact(firstname="new_fn"))
    app.session.logout()

def test_mod_lastname(app):
    app.session.login(username="admin",
                   password="secret")  # don't change because these fields will not changed(almost 100% only 2 parametrs)
    app.contact.modify_first(Contact(lastname="new_ln"))
    app.session.logout()

def test_mod_adress(app):
    app.session.login(username="admin",
                   password="secret")  # don't change because these fields will not changed(almost 100% only 2 parametrs)
    app.contact.modify_first(Contact(address="new_ad"))
    app.session.logout()

def test_mod_email(app):
    app.session.login(username="admin",
                   password="secret")  # don't change because these fields will not changed(almost 100% only 2 parametrs)
    app.contact.modify_first(Contact(email="new_em", email2="new_em2", email3="new_em3"))
    app.session.logout()

def test_mod_phones(app):
    app.session.login(username="admin",
                   password="secret")  # don't change because these fields will not changed(almost 100% only 2 parametrs)
    app.contact.modify_first(Contact(home="new_phh", mobile="new_phm", work="new_phw", fax="new_phf"))
    app.session.logout()