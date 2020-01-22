from model.group import Group


def test_add_group(app, json_groups): # json_groups for output in .py
    group = json_groups
    old_groups = app.group.get_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count_c()
    new_groups = app.group.get_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

