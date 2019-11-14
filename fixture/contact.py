# -*- coding: utf-8 -*-


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_add_form(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('[href="edit.php"]').click()

    def fill_form(self):
        wd = self.app.wd
        self.open_add_form()
        # fill form fields
        wd.find_element_by_name('firstname').click()
        wd.find_element_by_name('firstname').clear()
        wd.find_element_by_name('firstname').send_keys(contact.firstname)

