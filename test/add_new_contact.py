from all_info import Info
from fixture.applic import Applic
import pytest

@pytest.fixture
def app(request):
    fixture = Applic()
    request.addfinalizer(fixture.destr)
    return fixture

def test_add_new_contact(app):
    infoclass = Info("USA", "Colorado", "My notes about work", "My notes about work", "a@test.ru", "b@test.ru", "01-01-01", "02-02-02", "03-04-05", "06-07-08", "MyTitle", "MyCompany", "Russia", "Petrov", "Petr", "Petrovich", "Petya")
    app.session.login(username="admin", password="secret")
    app.contact.add_new()
    app.fio_fields(infoclass)
    app.about_company_fields(infoclass)
    app.telephones_fields(infoclass)
    app.emails_fields(infoclass)
    app.homepage_field("www.test.ru")
    app.birthday_fields()
    app.anniversary_fields()
    app.additional_fields(infoclass)
    app.contact.back_to_home_page()
    app.session.logout()
