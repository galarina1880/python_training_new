# -*- coding: utf-8 -*-


def test_del_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.del_first()
    app.session.logout()
