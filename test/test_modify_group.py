from model.group import Group

def test_modify_name(app):
    app.session.login(username="admin",
                   password="secret")  # don't change because these fields will not changed(almost 100% only 2 parametrs)
    app.group.modify_first(Group(name="New_training"))
    app.session.logout()

def test_modify_header(app):
    app.session.login(username="admin",
                   password="secret")  # don't change because these fields will not changed(almost 100% only 2 parametrs)
    app.group.modify_first(Group(header="New_header"))
    app.session.logout()

def test_modify_footer(app):
    app.session.login(username="admin",
                   password="secret")  # don't change because these fields will not changed(almost 100% only 2 parametrs)
    app.group.modify_first(Group(footer="New_footer"))
    app.session.logout()