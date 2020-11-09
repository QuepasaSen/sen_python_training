from selenium.webdriver.support.ui import Select

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_new(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def back_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home page").click()

    def create_contact(self, infoclass):
        wd = self.app.wd
        self.add_new()
        self.all_fields(infoclass)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.back_to_home_page()

    def delete_contact(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def edit_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        self.all_fields(contact)
        wd.find_element_by_name("update").click()

    def count_of_contact(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.get("http://localhost/addressbook/")
        return len(wd.find_elements_by_name("selected[]"))

    def change_field_of_contact_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def all_fields(self, all_info):
        wd = self.app.wd
        self.change_field_of_contact_value("address2", all_info.dop_address)
        self.change_field_of_contact_value("phone2", all_info.dop_phone)
        self.change_field_of_contact_value("notes", all_info.notes)
        self.change_field_of_contact_value("email", all_info.email)
        self.change_field_of_contact_value("email2", all_info.email2)
        self.change_field_of_contact_value("email3", all_info.email3)
        self.change_field_of_contact_value("home", all_info.domashniy)
        self.change_field_of_contact_value("mobile", all_info.mobilniy)
        self.change_field_of_contact_value("work", all_info.rabochiy)
        self.change_field_of_contact_value("fax", all_info.fax)
        self.change_field_of_contact_value("title", all_info.title)
        self.change_field_of_contact_value("company", all_info.company)
        self.change_field_of_contact_value("address", all_info.address)
        self.change_field_of_contact_value("firstname", all_info.firstname)
        self.change_field_of_contact_value("middlename", all_info.middlename)
        self.change_field_of_contact_value("lastname", all_info.lastname)
        self.change_field_of_contact_value("nickname", all_info.nickname)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("2")
        wd.find_element_by_xpath("(//option[@value='2'])[2]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("April")
        wd.find_element_by_xpath("(//option[@value='April'])[2]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").send_keys("2030")
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("1")
        wd.find_element_by_xpath("//option[@value='1']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("April")
        wd.find_element_by_xpath("//option[@value='April']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").send_keys("2020")
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("myhomepage.com")