from model.group import Group

def test_modify_name(app):
    app.group.modify_first(Group(name="New_training"))

def test_modify_header(app):
    app.group.modify_first(Group(header="New_header"))

def test_modify_footer(app):
    app.group.modify_first(Group(footer="New_footer"))
    