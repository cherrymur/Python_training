from model.group import Group

def test_add_group(app):
    app.group.create(Group(name="training", header="training", footer="training"))
    # app.session.logout() # break our test structure when we didn't have ensure_logout

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
