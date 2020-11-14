from model.group import Group

def test_group_add_ff(app):
    old_groups = app.group.get_group_list()
    app.group.create_group(Group(name="mynew", header="11", footer="22"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

def test_empty_group_add_ff(app):
    old_groups = app.group.get_group_list()
    app.group.create_group(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)