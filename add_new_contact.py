# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
from dop_info import Dop

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
        self.login(wd, username="admin", password="secret")
        self.add_new(wd)
        self.fio_fields(wd, firstname="Petrov", middlename="Petr", lastname="Petrovich", nickname="Petya")
        self.about_company_fields(wd, title="MyTitle", company="MyCompany", address="Russia")
        self.telephones_fields(wd, domashniy="01-01-01", mobilniy="02-02-02", rabochiy="03-04-05", fax="06-07-08")
        self.emails_fields(wd, email="test@mail.ru", email2="a@test.ru", email3="b@test.ru")
        self.homepage_field(wd, "www.test.ru")
        self.birthday_fields(wd)
        self.anniversary_fields(wd)
        self.additional_fields(wd, Dop(dop_address="USA", dop_phone="Colorado", notes="My notes about work"))
        self.back_to_home_page(wd)
        self.logout(wd)

    def additional_fields(self, wd, dop_info):
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").send_keys(dop_info.dop_address)
        wd.find_element_by_name("phone2").send_keys(dop_info.dop_phone)
        wd.find_element_by_name("notes").send_keys(dop_info.notes)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def back_to_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def anniversary_fields(self, wd):
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
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("1")
        wd.find_element_by_xpath("//option[@value='1']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("April")
        wd.find_element_by_xpath("//option[@value='April']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").send_keys("2020")

    def homepage_field(self, wd, homepage):
        wd.find_element_by_name("homepage").send_keys(homepage)

    def emails_fields(self, wd, email, email2, email3):
        wd.find_element_by_name("email").send_keys(email)
        wd.find_element_by_name("email2").send_keys(email2)
        wd.find_element_by_name("email3").send_keys(email3)

    def telephones_fields(self, wd, domashniy, mobilniy, rabochiy, fax):
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").send_keys(domashniy)
        wd.find_element_by_name("mobile").send_keys(mobilniy)
        wd.find_element_by_name("work").send_keys(rabochiy)
        wd.find_element_by_name("fax").send_keys(fax)

    def about_company_fields(self, wd, title, company, address):
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").send_keys(title)
        wd.find_element_by_name("company").send_keys(company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").send_keys(address)

    def fio_fields(self, wd, firstname, middlename, lastname, nickname):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").send_keys(firstname)
        wd.find_element_by_name("middlename").send_keys(middlename)
        wd.find_element_by_name("lastname").send_keys(lastname)
        wd.find_element_by_name("nickname").send_keys(nickname)

    def add_new(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/index.php")

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
