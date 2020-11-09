from model.all_info import Info

def test_edit_contact(app):
    if app.contact.count_of_contact() == 0:
        app.contact.create_contact(Info(firstname="Evgeny"))
    app.contact.edit_contact(Info(firstname="Gleb"))