from selenium.webdriver.support.ui import Select
from model.all_info import Info

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_new(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.current_url_check()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                lastname = element.find_element_by_xpath(".//td[2]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                firstname = element.find_element_by_xpath(".//td[3]").text
                all_phones = cells[5].text.splitlines()
                self.contact_cache.append(Info(lastname=lastname, firstname=firstname, id=id,
                                               domashniy=all_phones[0], mobilniy=all_phones[1],
                                               rabochiy=all_phones[2],dop_phone=all_phones[3]))
            return list(self.contact_cache)

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
        self.contact_cache = None

    def delete_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.current_url_check()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cache = None

    def current_url_check(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.get("http://localhost/addressbook/")

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.back_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def edit_contact(self):
        self.edit_contact_by_index(0)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.back_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()
        self.all_fields(contact)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def count_of_contact(self):
        wd = self.app.wd
        self.current_url_check()
        return len(wd.find_elements_by_name("selected[]"))

    def change_field_of_contact_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        domashniy = wd.find_element_by_name("home").get_attribute("value")
        rabochiy = wd.find_element_by_name("work").get_attribute("value")
        mobilniy = wd.find_element_by_name("mobile").get_attribute("value")
        dop_phone = wd.find_element_by_name("phone2").get_attribute("value")
        return Info(firstname=firstname, lastname=lastname, id=id, domashniy=domashniy, rabochiy=rabochiy, mobilniy=mobilniy, dop_phone=dop_phone)


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