from model.group import Group

def test_edit_first_group(app):
    group = Group(
        "testing",
        "11",
        "22")
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(group)
    app.session.logout()