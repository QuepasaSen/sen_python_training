from model.group import Group

def test_edit_group_name(app):
    old_groups = app.group.get_group_list()
    group = Group(name="New Name")
    group.id = old_groups[0].id
    if app.group.count_of_group() == 0:
        app.group.create_group(Group(name="test"))
    app.group.edit_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] == group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_edit_group_header(app):
#     old_groups = app.group.get_group_list()
#     if app.group.count_of_group() == 0:
#         app.group.create_group(Group(header="test"))
#     app.group.edit_first_group(Group(header="New Header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)

