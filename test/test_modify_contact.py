# -*- coding: utf-8 -*-
from model.contact import Contact


def test_mod_firstname(app):
    app.contact.modify_first(Contact(firstname="new_fn"))


def test_mod_lastname(app):
   app.contact.modify_first(Contact(lastname="new_ln"))


def test_mod_adress(app):
   app.contact.modify_first(Contact(address="new_ad"))


def test_mod_email(app):
   app.contact.modify_first(Contact(email="new_em", email2="new_em2", email3="new_em3"))


def test_mod_phones(app):
    app.contact.modify_first(Contact(home="new_phh", mobile="new_phm", work="new_phw", fax="new_phf"))
