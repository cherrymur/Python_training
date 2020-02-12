from pytest_bdd import given, when, then
from model.contact import Contact
import random


@given("a contact list")  # like a fixture
def contact_list(db):
    return db.get_contact_list()


@given("a contact with <firstname>, <middlename> and <lastname>")  # like a fixture
def new_contact(firstname, middlename, lastname):
    return Contact(firstname=firstname, middlename=middlename, lastname=lastname)


@when("I add the contact into the list")
def add_new_contact(app, new_contact):  # from Examples in contacts.feature
    app.contact.create(new_contact)


@then("the new contact list is equal to the old list with the added contact")
def verify_contact_added(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@given("a non-empty contact list")  # like a fixture
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(name="some name"))
    return db.get_contact_list()


@given("a random contact from the list")  # like a fixture
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when("I delete the contact from the list")
def delete_random_contact(app, random_contact): # from Examples in contacts.feature
    app.contact.delete_by_id(random_contact.id)


@then("the new contact list is equal to the old list without the deleted contact")
def verify_contact_added(db, non_empty_contact_list, random_contact, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(random_contact)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_list(), key=Contact.id_or_max)