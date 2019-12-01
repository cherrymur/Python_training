def test_del_first_group(app):
    app.session.login(username="admin",
                   password="secret")  # don't change because these fields will not changed(almost 100% only 2 parametrs)
    app.contact.delete_first()
    app.session.logout()