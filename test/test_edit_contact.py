from model.all_info import Info
from random import randrange

def test_edit_contact(app):
    if app.contact.count_of_contact() == 0:
        app.contact.create_contact(Info(firstname="Evgeny", lastname="Nikolaevich"))
    old_contact_list = app.contact.get_contact_list()
    index = randrange(len(old_contact_list))
    newname = Info(firstname="Boris", lastname="Borisovich")
    newname.id = old_contact_list[index].id
    app.contact.edit_contact_by_index(index, newname)
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) == len(new_contact_list)
    old_contact_list[index] = newname
    assert sorted(old_contact_list, key=Info.id_or_max) == sorted(new_contact_list, key=Info.id_or_max)