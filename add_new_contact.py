# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
from all_info import info

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
        self.fio_fields(wd, info(firstname="Petrov", middlename="Petr", lastname="Petrovich", nickname="Petya"))
        self.about_company_fields(wd, info(title="MyTitle", company="MyCompany", address="Russia"))
        self.telephones_fields(wd, info(domashniy="01-01-01", mobilniy="02-02-02", rabochiy="03-04-05", fax="06-07-08"))
        self.emails_fields(wd, info(email="test@mail.ru", email2="a@test.ru", email3="b@test.ru"))
        self.homepage_field(wd, "www.test.ru")
        self.birthday_fields(wd)
        self.anniversary_fields(wd)
        self.additional_fields(wd, info(dop_address="USA", dop_phone="Colorado", notes="My notes about work"))
        self.back_to_home_page(wd)
        self.logout(wd)

    def additional_fields(self, wd, all_info):
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").send_keys(all_info.dop_address)
        wd.find_element_by_name("phone2").send_keys(all_info.dop_phone)
        wd.find_element_by_name("notes").send_keys(all_info.notes)
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

    def emails_fields(self, wd, all_info):
        wd.find_element_by_name("email").send_keys(all_info.email)
        wd.find_element_by_name("email2").send_keys(all_info.email2)
        wd.find_element_by_name("email3").send_keys(all_info.email3)

    def telephones_fields(self, wd, all_info):
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").send_keys(all_info.domashniy)
        wd.find_element_by_name("mobile").send_keys(all_info.mobilniy)
        wd.find_element_by_name("work").send_keys(all_info.rabochiy)
        wd.find_element_by_name("fax").send_keys(all_info.fax)

    def about_company_fields(self, wd, all_info):
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").send_keys(all_info.title)
        wd.find_element_by_name("company").send_keys(all_info.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").send_keys(all_info.address)

    def fio_fields(self, wd, all_info):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").send_keys(all_info.firstname)
        wd.find_element_by_name("middlename").send_keys(all_info.middlename)
        wd.find_element_by_name("lastname").send_keys(all_info.lastname)
        wd.find_element_by_name("nickname").send_keys(all_info.nickname)

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
