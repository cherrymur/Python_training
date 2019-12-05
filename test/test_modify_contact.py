# -*- coding: utf-8 -*-
def test_mod_first_contact(app):
    app.session.login(username="admin",
                   password="secret")  # don't change because these fields will not changed(almost 100% only 2 parametrs)
    app.contact.modify_first()
    app.session.logout()