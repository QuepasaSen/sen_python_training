from model.group import Group
from random import randrange

def test_edit_group_name(app):
    if app.group.count_of_group() == 0:
        app.group.create_group(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New Name")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_edit_group_header(app):
#     old_groups = app.group.get_group_list()
#     if app.group.count_of_group() == 0:
#         app.group.create_group(Group(header="test"))
#     app.group.edit_first_group(Group(header="New Header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)

