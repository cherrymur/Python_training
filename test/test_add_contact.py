# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.contact.add(Contact(firstname="Avramenko", middlename="Olga", lastname="shdjs", nickname="cherrymur",
                            title="dshdj", company="hjhj", address="hjhj", home="hj", mobile="hjh", work="hjh", fax="hjhj",
                            email="ghgh", email2="hgh", email3="hgh", homepage="hghg", bday="31", bmonth="December", byear="1990",
                            aday="12", amonth="October", ayear="1236", address2="dsfef", phone2="sas", notes="dsd"))
