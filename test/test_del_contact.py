from model.contact import Contact


def test_del_first_contact(app):
    if app.contact.count_c() == 0:
        app.contact.create(Contact(firstname="Avramenko", middlename="Olga", lastname="shdjs"))
    app.contact.delete_first()
