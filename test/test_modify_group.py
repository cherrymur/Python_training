from model.group import Group
import random


def test_modify_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="training", header="training", footer="training"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    index = old_groups.index(group)
    added_group = Group(name="New_training")
    added_group.id = group.id
    app.group.modify_by_id(group.id, added_group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = added_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui: # flag to on/off assert
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_list(), key=Group.id_or_max)


#def test_modify_header(app):
 #   if app.group.count() == 0:
  #      app.group.create(Group(name="training", header="training", footer="training"))
   # old_groups = app.group.get_groups_list()
    #app.group.modify_first(Group(header="New_header"))
    #new_groups = app.group.get_groups_list()
    #assert len(old_groups) == len(new_groups)


#def test_modify_footer(app):
 #   if app.group.count() == 0:
  #      app.group.create(Group(name="training", header="training", footer="training"))
   # old_groups = app.group.get_groups_list()
    #app.group.modify_first(Group(footer="New_footer"))
    #new_groups = app.group.get_groups_list()
    #assert len(old_groups) == len(new_groups)
