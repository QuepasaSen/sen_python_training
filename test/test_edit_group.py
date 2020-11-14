from model.group import Group

def test_edit_group_name(app):
    old_groups = app.group.get_group_list()
    if app.group.count_of_group() == 0:
        app.group.create_group(Group(name="test"))
    app.group.edit_first_group(Group(name="New Name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_edit_group_header(app):
    old_groups = app.group.get_group_list()
    if app.group.count_of_group() == 0:
        app.group.create_group(Group(header="test"))
    app.group.edit_first_group(Group(header="New Header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

