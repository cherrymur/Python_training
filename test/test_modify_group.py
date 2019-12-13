from model.group import Group


def test_modify_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="training", header="training", footer="training"))
    old_groups = app.group.get_groups_list()
    app.group.modify_first(Group(name="New_training"))
    new_groups = app.group.get_groups_list()
    assert len(old_groups) == len(new_groups)


def test_modify_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="training", header="training", footer="training"))
    old_groups = app.group.get_groups_list()
    app.group.modify_first(Group(header="New_header"))
    new_groups = app.group.get_groups_list()
    assert len(old_groups) == len(new_groups)


def test_modify_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="training", header="training", footer="training"))
    old_groups = app.group.get_groups_list()
    app.group.modify_first(Group(footer="New_footer"))
    new_groups = app.group.get_groups_list()
    assert len(old_groups) == len(new_groups)
