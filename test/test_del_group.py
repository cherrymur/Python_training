from model.group import Group


# preconditions are about test procedure, not about fixture
#Fixture should be static
def test_del_first_group(app):
    # check that one or more contact exist
    if app.group.count() == 0:
        app.group.create(Group(name="training", header="training", footer="training"))
    app.group.delete_first()
