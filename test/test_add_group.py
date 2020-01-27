from model.group import Group


def test_add_group(app, db, json_groups, check_ui): # json_groups for output in .py
    group = json_groups
    old_groups = db.get_group_list() # get info from db
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui: # flag to on/off assert
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_list(), key=Group.id_or_max)

