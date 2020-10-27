# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest

class AddNewContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_new_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.add_new(wd)
        self.fio_fields(wd)
        self.about_company_fields(wd)
        self.telephones_fields(wd)
        self.emails_fields(wd)
        self.homepage_field(wd)
        self.birthday_fields(wd)
        self.anniversary_fields(wd)
        self.additional_fields(wd)

    def additional_fields(self, wd):
        # additional information
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").send_keys("USA")
        wd.find_element_by_name("phone2").send_keys("Colorado")
        wd.find_element_by_name("notes").send_keys("My notes about work")
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        wd.find_element_by_link_text("home page").click()
        wd.find_element_by_link_text("Logout").click()

    def anniversary_fields(self, wd):
        # anniversary
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("2")
        wd.find_element_by_xpath("(//option[@value='2'])[2]").click()
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("April")
        wd.find_element_by_xpath("(//option[@value='April'])[2]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").send_keys("2030")
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("ayear").click()

    def birthday_fields(self, wd):
        # birthday
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("1")
        wd.find_element_by_xpath("//option[@value='1']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("April")
        wd.find_element_by_xpath("//option[@value='April']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").send_keys("2020")

    def homepage_field(self, wd):
        # homepage adress
        wd.find_element_by_name("homepage").send_keys("www.test.ru")

    def emails_fields(self, wd):
        # emails
        wd.find_element_by_name("email").send_keys("test@mail.ru")
        wd.find_element_by_name("email2").send_keys("a@test.ru")
        wd.find_element_by_name("email3").send_keys("b@test.ru")

    def telephones_fields(self, wd):
        # telephone numbers
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").send_keys("01-01-01")
        wd.find_element_by_name("mobile").send_keys("02-02-02")
        wd.find_element_by_name("work").send_keys("03-04-05")
        wd.find_element_by_name("fax").send_keys("06-07-08")

    def about_company_fields(self, wd):
        # fields about company
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").send_keys("MyTitle")
        wd.find_element_by_name("company").send_keys("MyCompany")
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").send_keys("Russia")

    def fio_fields(self, wd):
        # fill fio fields
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").send_keys("Petrov")
        wd.find_element_by_name("middlename").send_keys("Petr")
        wd.find_element_by_name("lastname").send_keys("Petrovich")
        wd.find_element_by_name("nickname").send_keys("Petya")

    def add_new(self, wd):
        # add new contact
        wd.find_element_by_link_text("add new").click()

    def login(self, wd):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        # open home page
        wd.get("http://localhost/addressbook/index.php")

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()