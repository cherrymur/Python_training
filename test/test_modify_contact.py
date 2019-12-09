# -*- coding: utf-8 -*-
from model.contact import Contact


def test_mod_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Avramenko", middlename="Olga", lastname="shdjs", nickname="cherrymur",
                                   title="dshdj", company="hjhj", address="hjhj", home="hj", mobile="hjh", work="hjh",
                                   fax="hjhj",
                                   email="ghgh", email2="hgh", email3="hgh", homepage="hghg", bday="31",
                                   bmonth="December", byear="1990",
                                   aday="12", amonth="October", ayear="1236", address2="dsfef", phone2="sas",
                                   notes="dsd"))
    app.contact.modify_first(Contact(firstname="new_fn"))


def test_mod_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Avramenko", middlename="Olga", lastname="shdjs", nickname="cherrymur",
                                   title="dshdj", company="hjhj", address="hjhj", home="hj", mobile="hjh", work="hjh",
                                   fax="hjhj",
                                   email="ghgh", email2="hgh", email3="hgh", homepage="hghg", bday="31",
                                   bmonth="December", byear="1990",
                                   aday="12", amonth="October", ayear="1236", address2="dsfef", phone2="sas",
                                   notes="dsd"))
    app.contact.modify_first(Contact(lastname="new_ln"))


def test_mod_adress(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Avramenko", middlename="Olga", lastname="shdjs", nickname="cherrymur",
                                   title="dshdj", company="hjhj", address="hjhj", home="hj", mobile="hjh", work="hjh",
                                   fax="hjhj",
                                   email="ghgh", email2="hgh", email3="hgh", homepage="hghg", bday="31",
                                   bmonth="December", byear="1990",
                                   aday="12", amonth="October", ayear="1236", address2="dsfef", phone2="sas",
                                   notes="dsd"))
    app.contact.modify_first(Contact(address="new_ad"))


def test_mod_email(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Avramenko", middlename="Olga", lastname="shdjs", nickname="cherrymur",
                                   title="dshdj", company="hjhj", address="hjhj", home="hj", mobile="hjh", work="hjh",
                                   fax="hjhj",
                                   email="ghgh", email2="hgh", email3="hgh", homepage="hghg", bday="31",
                                   bmonth="December", byear="1990",
                                   aday="12", amonth="October", ayear="1236", address2="dsfef", phone2="sas",
                                   notes="dsd"))
    app.contact.modify_first(Contact(email="new_em", email2="new_em2", email3="new_em3"))


def test_mod_phones(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Avramenko", middlename="Olga", lastname="shdjs", nickname="cherrymur",
                                   title="dshdj", company="hjhj", address="hjhj", home="hj", mobile="hjh", work="hjh",
                                   fax="hjhj",
                                   email="ghgh", email2="hgh", email3="hgh", homepage="hghg", bday="31",
                                   bmonth="December", byear="1990",
                                   aday="12", amonth="October", ayear="1236", address2="dsfef", phone2="sas",
                                   notes="dsd"))
    app.contact.modify_first(Contact(home="new_phh", mobile="new_phm", work="new_phw", fax="new_phf"))
