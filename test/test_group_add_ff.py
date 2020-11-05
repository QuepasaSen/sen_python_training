# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_group_add_ff(app):
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.create(Group(name="mynew", header="11", footer="22"))
    app.session.logout()

def test_empty_group_add_ff(app):
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()