# -*- coding: utf-8 -*-
from model.contact import Contact


def test_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify(Contact(firstname='fname mod', mname='mname mod', lastname='lname mod', nickname='nickname mod', title='title mod', company='company mod', address1='addr1 mod', telhome='12345 mod', telmobile='812345 mod', telwork='54321 mod', fax='55555 mod', email1='email 1 mod', email2='emqil 2 mod', email3='email 3 mod', homepage='HP mod', bday='10', bmonth='September', byear='19885', aday='8', amonth='September', ayear='2025', address2='address 2 mod', phone2='phone 2 mod', notes='notes mod'))
    app.session.logout()
