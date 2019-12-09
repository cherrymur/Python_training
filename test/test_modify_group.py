from model.group import Group


def test_modify_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="training", header="training", footer="training"))
    app.group.modify_first(Group(name="New_training"))


def test_modify_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="training", header="training", footer="training"))
    app.group.modify_first(Group(header="New_header"))


def test_modify_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="training", header="training", footer="training"))
    app.group.modify_first(Group(footer="New_footer"))
