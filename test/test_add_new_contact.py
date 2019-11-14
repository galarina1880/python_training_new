# -*- coding: utf-8 -*-
from model.contact import Contact


def test_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.fill_form(Contact(firstname='fname', mname='mname', lastname='lname', nickname='nickname', title='title', company='company', address1='addr1', telhome='12345', telmobile='812345', telwork='54321', fax='55555', email1='email 1', email2='emqil 2', email3='email 3', homepage='HP', bday='6', bmonth='August', byear='1980', aday='6', amonth='August', ayear='2020', address2='address 2', phone2='phone 2', notes='notes'))
    app.session.logout()


def test_new_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.fill_form(Contact(firstname='', mname='', lastname='', nickname='', title='', company='', address1='', telhome='', telmobile='', telwork='', fax='', email1='', email2='', email3='', homepage='', bday='-', bmonth='-', byear='', aday='-', amonth='-', ayear='', address2='', phone2='', notes=''))
    app.session.logout()
