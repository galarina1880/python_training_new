# -*- coding: utf-8 -*-
from model.group import Group


def test_new_group(app):
    app.session.login(username="admin", password="secret")
    app.group.add_new(Group(name="gr1", header="header 1", footer="footer 1"))
    app.session.logout()


def test_new_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.add_new(Group(name="", header="", footer=""))
    app.session.logout()
