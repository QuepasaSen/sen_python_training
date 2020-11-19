from model.all_info import Info
from random import randrange

def test_delete_contact(app):
    if app.contact.count_of_contact() == 0:
        app.contact.create_contact(Info(firstname="Evgeny"))
    old_contact_list = app.contact.get_contact_list()
    index = randrange(len(old_contact_list))
    app.contact.delete_contact_by_index(index)
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) - 1 == len(new_contact_list)
    old_contact_list[index:index+1] = []
    assert old_contact_list == new_contact_list