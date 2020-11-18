from model.group import Group

def test_group_add_ff(app):
    old_groups = app.group.get_group_list()
    group = Group(name="mynew", header="11", footer="22")
    app.group.create_group(group)
    assert len(old_groups) + 1 == app.group.count_of_group()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_empty_group_add_ff(app):
#     old_groups = app.group.get_group_list()
#     group = Group(name="", header="", footer="")
#     app.group.create_group(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) + 1 == len(new_groups)
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)