from model.all_info import Info

def test_edit_contact(app):
    contact = Info(
        "USA",
        "Colorado",
        "My notes about work",
        "My notes about work",
        "a@test.ru",
        "b@test.ru",
        "01-01-01",
        "02-02-02",
        "03-04-05",
        "06-07-08",
        "MyTitle",
        "MyCompany",
        "Russia",
        "Ivanov",
        "Petr",
        "Petrovich",
        "Petya")
    app.session.login(username="admin", password="secret")
    app.contact.edit_contact(contact)
    app.session.logout()