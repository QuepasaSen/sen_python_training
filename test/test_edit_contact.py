from model.all_info import Info

def test_edit_contact(app):
    contact = Info(
        "Russia",
        "Saint-Petersburg",
        "My notes not about work",
        "My notes not about work",
        "a1@test.ru",
        "b1@test.ru",
        "11-11-11",
        "22-22-22",
        "33-44-55",
        "66-77-88",
        "Not MyTitle",
        "Not MyCompany",
        "USA",
        "Ivanov",
        "Ivan",
        "Ivanovich",
        "Vanya")
    app.session.login(username="admin", password="secret")
    app.contact.edit_contact(contact)
    app.session.logout()