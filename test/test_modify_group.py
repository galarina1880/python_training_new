# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.open_first_for_edit(Group(name="gr1 mod", header="header 1 mod", footer="footer 1 mod"))
    app.session.logout()
