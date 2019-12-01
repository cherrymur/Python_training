from model.group import Group

def test_add_group(app):
    app.session.login(username="admin",
                   password="secret")  # don't change because these fields will not changed(almost 100% only 2 parametrs)
    app.group.create(Group(name="training", header="training", footer="training"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()