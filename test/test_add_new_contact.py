from model.all_info import Info

def test_add_new_contact(app):
    old_contact_list = app.contact.get_contact_list()
    infoclass = Info("USA", "Colorado", "My notes about work", "My notes about work", "a@test.ru", "b@test.ru", "01-01-01", "02-02-02", "03-04-05", "06-07-08", "MyTitle", "MyCompany", "Russia", "Petrov", "Petr", "Petrovich", "Petya")
    app.contact.create_contact(infoclass)
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) + 1 == len(new_contact_list)
    old_contact_list.append(infoclass)
    print(new_contact_list)
    print(old_contact_list)
    assert sorted(old_contact_list, key=Info.id_or_max) == sorted(new_contact_list, key=Info.id_or_max)
