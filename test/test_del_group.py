from model.group import Group
from random import randrange


# preconditions are about test procedure, not about fixture
# Fixture should be static
def test_del_some_group(app):
    # check that one or more contact exist
    if app.group.count_c() == 0:
        app.group.create(Group(name="training", header="training", footer="training"))
    old_groups = app.group.get_list()
    index = randrange(len(old_groups))
    app.group.delete_by_index(index)
    assert len(old_groups) - 1 == app.group.count_c()
    new_groups = app.group.get_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups
