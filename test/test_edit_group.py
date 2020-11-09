from model.group import Group

def test_edit_group_name(app):
    if app.group.count_of_group() == 0:
        app.group.create_group(Group(name="test"))
    app.group.edit_first_group(Group(name="New Name"))

def test_edit_group_header(app):
    if app.group.count_of_group() == 0:
        app.group.create_group(Group(header="test"))
    app.group.edit_first_group(Group(header="New Header"))

