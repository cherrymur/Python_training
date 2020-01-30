# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_mod_firstname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Avramenko", middlename="Olga", lastname="shdjs", nickname="cherrymur",
                                   title="dshdj", company="hjhj", address="hjhj", homephone="hj", mobilephone="hjh", workphone="hjh",
                                   faxphone="hjhj",
                                   email="ghgh", email2="hgh", email3="hgh", homepage="hghg", bday="31",
                                   bmonth="December", byear="1990",
                                   aday="12", amonth="October", ayear="1236", address2="dsfef", secondaryphone="sas",
                                   notes="dsd"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    index = old_contacts.index(contact)
    added_contact = Contact(firstname="new_fn")
    added_contact.id = contact.id
    app.contact.modify_by_id(contact.id, added_contact)
    added_contact.lastname = old_contacts[index].lastname
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = added_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui: # flag to on/off assert
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_list(), key=Contact.id_or_max)


'''
def test_mod_lastname(app):
    if app.contact.count_c() == 0:
        app.contact.create(Contact(firstname="Avramenko", middlename="Olga", lastname="shdjs", nickname="cherrymur",
                                   title="dshdj", company="hjhj", address="hjhj", home="hj", mobile="hjh", work="hjh",
                                   fax="hjhj",
                                   email="ghgh", email2="hgh", email3="hgh", homepage="hghg", bday="31",
                                   bmonth="December", byear="1990",
                                   aday="12", amonth="October", ayear="1236", address2="dsfef", secondaryphone="sas",
                                   notes="dsd"))
    old_contacts = app.contact.get_list()
    index = randrange(len(old_contacts))
    added_contact = Contact(lastname="new_ln")
    added_contact.id = old_contacts[index].id
    added_contact.firstname = old_contacts[index].firstname
    app.contact.modify_by_index(index, added_contact)
    assert len(old_contacts) == app.contact.count_c()
    new_contacts = app.contact.get_list()
    old_contacts[index] = added_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_mod_adress(app):
 #   if app.contact.count() == 0:
  #      app.contact.create(Contact(firstname="Avramenko", middlename="Olga", lastname="shdjs", nickname="cherrymur",
   #                                title="dshdj", company="hjhj", address="hjhj", home="hj", mobile="hjh", work="hjh",
    #                               fax="hjhj",
     ###                             aday="12", amonth="October", ayear="1236", address2="dsfef", phone2="sas",
        #                           notes="dsd"))
#    app.contact.modify_first(Contact(address="new_ad"))


#def test_mod_email(app):
 #   if app.contact.count() == 0:
  #      app.contact.create(Contact(firstname="Avramenko", middlename="Olga", lastname="shdjs", nickname="cherrymur",
   #                                title="dshdj", company="hjhj", address="hjhj", home="hj", mobile="hjh", work="hjh",
    #                               fax="hjhj",
     ###                             aday="12", amonth="October", ayear="1236", address2="dsfef", phone2="sas",
        #                           notes="dsd"))
   # app.contact.modify_first(Contact(email="new_em", email2="new_em2", email3="new_em3"))


### def test_mod_phones(app):
    #if app.contact.count() == 0:
     #   app.contact.create(Contact(firstname="Avramenko", middlename="Olga", lastname="shdjs", nickname="cherrymur",
      #                             title="dshdj", company="hjhj", address="hjhj", home="hj", mobile="hjh", work="hjh",
       ##                           email="ghgh", email2="hgh", email3="hgh", homepage="hghg", bday="31",
         #                          bmonth="December", byear="1990",
          #                         aday="12", amonth="October", ayear="1236", address2="dsfef", phone2="sas",
           #                        notes="dsd"))
    # app.contact.modify_first(Contact(home="new_phh", mobile="new_phm", work="new_phw", fax="new_phf"))
'''