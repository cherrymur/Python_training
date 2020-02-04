import re
from model.contact import Contact


def test_contacts_on_home_page_w_db(app, db):
    if len(app.contact.get_list()) == 0:
        app.contact.create(Contact(firstname="Avramenko", middlename="Olga", lastname="shdjs", nickname="cherrymur",
                                   title="dshdj", company="hjhj", address="hjhj", homephone="hj", mobilephone="hjh", workphone="hjh",
                                   faxphone="hjhj",
                                   email="ghgh", email2="hgh", email3="hgh", homepage="hghg", bday="31",
                                   bmonth="December", byear="1990",
                                   aday="12", amonth="October", ayear="1236", address2="dsfef", secondaryphone="sas",
                                   notes="dsd"))
    list_contacts_from_homepage = sorted(app.contact.get_list(), key=Contact.id_or_max)
    list_contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert list_contacts_from_homepage == list_contacts_from_db
    for i in range(len(list_contacts_from_homepage)):
        contact = list_contacts_from_db[i]
        assert clear(list_contacts_from_homepage[i].all_phones_from_home_page) == merge_phones_like_on_home_page(contact)
        assert clear(list_contacts_from_homepage[i].all_emails_from_home_page) == merge_emails_like_on_home_page(contact)
        assert list_contacts_from_homepage[i].firstname == contact.firstname
        assert list_contacts_from_homepage[i].lastname == contact.lastname
        assert list_contacts_from_homepage[i].address == contact.address

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