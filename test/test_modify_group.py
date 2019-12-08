from model.group import Group


# preconditions are about test procedure, not about common configuration
def test_modify_name(app):
    # check that one or more group exist
    if app.group.count() == 0:
        app.group.create(Group(name="training", header="training", footer="training"))
    if app.group.is_empty("group_name"):
        app.group.modify_first(Group(name="new_training"))
    else:
        app.group.modify_first(Group(name=""))


def test_modify_header(app):
    # check that one or more group exist
    if app.group.count() == 0:
        app.group.create(Group(name="training", header="training", footer="training"))
    if app.group.is_empty("group_header"):
        app.group.modify_first(Group(header="New_header"))
    else:
        app.group.modify_first(Group(header=""))

def test_modify_footer(app):
    # check that one or more group exist
    if app.group.count() == 0:
        app.group.create(Group(name="training", header="training", footer="training"))
    if app.group.is_empty("group_footer"):
        app.group.modify_first(Group(footer="New_footer"))
    else:
        app.group.modify_first(Group(footer=""))
