from model.group import Group


# preconditions are about test procedure, not about fixture
# Fixture should be static
def test_del_first_group(app):
    # check that one or more contact exist
    if app.group.count_c() == 0:
        app.group.create(Group(name="training", header="training", footer="training"))
    old_groups = app.group.get_list()
    app.group.delete_first()
    new_groups = app.group.get_list()
    assert (len(old_groups) - 1) == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups
