from model.all_info import Info

def test_add_new_contact(app):
    old_contact_list = app.contact.get_contact_list()
    infoclass = Info("USA", "406214", "My notes about work", "My notes about work", "a@test.ru", "b@test.ru", "01-01-01", "02-02-02", "03-04-05", "06-07-08", "MyTitle", "MyCompany", "Russia", "Petrov", "Petr", "Petrovich", "Petya")
    app.contact.create_contact(infoclass)
    assert len(old_contact_list) + 1 == app.contact.count_of_contact()
    new_contact_list = app.contact.get_contact_list()
    old_contact_list.append(infoclass)
    assert sorted(old_contact_list, key=Info.id_or_max) == sorted(new_contact_list, key=Info.id_or_max)
