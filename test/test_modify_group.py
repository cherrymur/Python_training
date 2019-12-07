from model.group import Group

def test_del_first_group(app):
    app.session.login(username="admin",
                   password="secret")  # don't change because these fields will not changed(almost 100% only 2 parametrs)
    app.group.modify_first(Group(name="New_training", header="new_header", footer="new_footer"))
    app.session.logout()