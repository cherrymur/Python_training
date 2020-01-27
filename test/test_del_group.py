from model.group import Group
import random


# preconditions are about test procedure, not about fixture
# Fixture should be static
def test_del_some_group(app, db):
    # check that one or more contact exist
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="training", header="training", footer="training"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
