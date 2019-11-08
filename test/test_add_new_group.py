# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_new_group(app):
    app.session.login(username="admin", password="secret")
    app.group.add_new_group(Group(name="gr1", header="header 1", footer="footer 1"))
    app.session.logout()


def test_new_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.add_new_group(Group(name="", header="", footer=""))
    app.session.logout()
