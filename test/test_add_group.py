from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_list()
    added_group = Group(name="training", header="training", footer="training")
    app.group.create(added_group)
    # app.session.logout() # break our test structure when we didn't have ensure_logout
    new_groups = app.group.get_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(added_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups,key=Group.id_or_max)


def test_add_empty_group(app):
    old_groups = app.group.get_list()
    added_group = Group(name="", header="", footer="")
    app.group.create(added_group)
    new_groups = app.group.get_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(added_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups,key=Group.id_or_max)
