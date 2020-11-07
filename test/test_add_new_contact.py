from model.all_info import Info
from fixture.application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_contact(app):
    infoclass = Info("USA", "Colorado", "My notes about work", "My notes about work", "a@test.ru", "b@test.ru", "01-01-01", "02-02-02", "03-04-05", "06-07-08", "MyTitle", "MyCompany", "Russia", "Petrov", "Petr", "Petrovich", "Petya")
    app.session.login(username="admin", password="secret")
    app.contact.add_new()
    app.contact.fio_fields(infoclass)
    app.contact.about_company_fields(infoclass)
    app.contact.telephones_fields(infoclass)
    app.contact.emails_fields(infoclass)
    app.contact.homepage_field("www.test.ru")
    app.contact.birthday_fields()
    app.contact.anniversary_fields()
    app.contact.additional_fields(infoclass)
    app.contact.back_to_home_page()
    app.session.logout()
