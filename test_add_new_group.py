# -*- coding: utf-8 -*-
from selenium import webdriver
from group import Group
import unittest


class NewGroup1(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def add_new_group(self, group):
        wd = self.wd
        self.open_groups_page()
        # open new group add form
        wd.find_element_by_name("new").click()
        # fill out new group form ans save new group
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        self.open_groups_page()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def test_new_group(self):
        self.login(username="admin", password="secret")
        self.add_new_group(Group(name="gr1", header="header 1", footer="footer 1"))
        self.logout()

    def test_new_empty_group(self):
        self.login(username="admin", password="secret")
        self.add_new_group(Group(name="", header="", footer=""))
        self.logout()

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
