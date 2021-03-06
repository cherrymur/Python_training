import re
from random import randrange


def test_phones_on_home_page(app):
    list_contacts = app.contact.get_list()
    index = randrange(len(list_contacts))
    contact_from_home_page = list_contacts[index]
    contact_from_edit_page = app.contact.get_info_from_edit_page(index)
    assert clear(contact_from_home_page.all_phones_from_home_page) == merge_phones_like_on_home_page(contact_from_edit_page)
    assert clear(contact_from_home_page.all_emails_from_home_page) == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.address == contact_from_edit_page.address

# def test_phones_on_contact_view_page(app):
  #   list_contacts = app.contact.get_list()
    #index = randrange(len(list_contacts))
    #contact_from_view_page = app.contact.get_contact_from_view_page(index)
    #contact_from_edit_page = app.contact.get_info_from_edit_page(index)
    #assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    #assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    #assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    #assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone
    #assert contact_from_view_page.email == contact_from_edit_page.email
    #assert contact_from_view_page.email2 == contact_from_edit_page.email2
    #assert contact_from_view_page.email3 == contact_from_edit_page.email3


def merge_emails_like_on_home_page(contact):
    list = "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))
    return list

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone,
                                        contact.secondaryphone]))))