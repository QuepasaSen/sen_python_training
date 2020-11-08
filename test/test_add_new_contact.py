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
    app.contact.create_contact(infoclass)
    app.session.logout()
