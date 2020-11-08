from model.group import Group

def test_group_add_ff(app):
    app.group.create_group(Group(name="mynew", header="11", footer="22"))

def test_empty_group_add_ff(app):
    app.group.create_group(Group(name="", header="", footer=""))