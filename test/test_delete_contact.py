from model.all_info import Info

def test_delete_contact(app):
    if app.contact.count_of_contact() == 0:
        app.contact.create_contact(Info(firstname="Evgeny"))
    old_contact_list = app.contact.get_contact_list()
    app.contact.delete_contact()
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) - 1 == len(new_contact_list)
    old_contact_list[0:1] = []
    assert old_contact_list == new_contact_list