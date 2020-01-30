import re
from random import randrange
from model.contact import Contact


def test_contacts_home_page(app, db):
    list_contacts = app.contact.get_list()
    assert sorted(list_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)

'''    
    index = randrange(len(list_contacts)-1)
    contact_from_home_page = list_contacts[index]
    contact_from_edit_page = app.contact.get_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.address == contact_from_edit_page.address
    
def test_phones_on_contact_view_page(app):
    list_contacts = app.contact.get_list()
    index = randrange(len(list_contacts))
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact.get_info_from_edit_page(index)
    assert merge_phones_like_on_home_page(contact_from_view_page) == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_view_page.all_emails_from_view_page == merge_emails_like_on_home_page(contact_from_edit_page)
    #assert contact_from_home_page.address == contact_from_edit_page.address


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))

def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone,
                                        contact.secondaryphone]))))
'''