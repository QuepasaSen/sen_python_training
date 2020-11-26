from model.all_info import Info
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phone(prefix, maxlen):
    symbols = "+" + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Info(dop_address=random_string("dop_address", 10), notes=random_string("notes", 20), email=random_string("email", 20),
                 email2=random_string("email2", 20), email3=random_string("email3", 20), title=random_string("title", 20), company=random_string("company", 20),
                 address=random_string("address", 20), firstname=random_string("firstname", 20), middlename=random_string("middlename", 20), lastname=random_string("lastname", 20),
                 nickname=random_string("nickname", 20), dop_phone=random_phone("dop_phone", 11), domashniy=random_phone("domashniy", 11), mobilniy=random_phone("mobilniy", 11),
                 rabochiy=random_phone("rabochiy", 11), fax=random_phone("fax", 11))
    for i in range(2)
]

# self.change_field_of_contact_value("address2", all_info.dop_address)
#         self.change_field_of_contact_value("phone2", all_info.dop_phone)
#         self.change_field_of_contact_value("notes", all_info.notes)
#         self.change_field_of_contact_value("email", all_info.email)
#         self.change_field_of_contact_value("email2", all_info.email2)
#         self.change_field_of_contact_value("email3", all_info.email3)
#         self.change_field_of_contact_value("home", all_info.domashniy)
#         self.change_field_of_contact_value("mobile", all_info.mobilniy)
#         self.change_field_of_contact_value("work", all_info.rabochiy)
#         self.change_field_of_contact_value("fax", all_info.fax)
#         self.change_field_of_contact_value("title", all_info.title)
#         self.change_field_of_contact_value("company", all_info.company)
#         self.change_field_of_contact_value("address", all_info.address)
#         self.change_field_of_contact_value("firstname", all_info.firstname)
#         self.change_field_of_contact_value("middlename", all_info.middlename)
#         self.change_field_of_contact_value("lastname", all_info.lastname)
#         self.change_field_of_contact_value("nickname", all_info.nickname)
#         wd.find_element_by_name("aday").click()
#         Select(wd.find_element_by_name("aday")).select_by_visible_text("2")
#         wd.find_element_by_xpath("(//option[@value='2'])[2]").click()
#         wd.find_element_by_name("amonth").click()
#         Select(wd.find_element_by_name("amonth")).select_by_visible_text("April")
#         wd.find_element_by_xpath("(//option[@value='April'])[2]").click()
#         wd.find_element_by_name("ayear").click()
#         wd.find_element_by_name("ayear").send_keys("2030")
#         wd.find_element_by_name("ayear").click()
#         wd.find_element_by_name("bday").click()
#         Select(wd.find_element_by_name("bday")).select_by_visible_text("1")
#         wd.find_element_by_xpath("//option[@value='1']").click()
#         wd.find_element_by_name("bmonth").click()
#         Select(wd.find_element_by_name("bmonth")).select_by_visible_text("April")
#         wd.find_element_by_xpath("//option[@value='April']").click()
#         wd.find_element_by_name("byear").click()
#         wd.find_element_by_name("byear").send_keys("2020")
#         wd.find_element_by_name("homepage").click()
#         wd.find_element_by_name("homepage").clear()
#         wd.find_element_by_name("homepage").send_keys("myhomepage.com")

@pytest.mark.parametrize("contact", testdata,ids=[repr(x) for x in testdata])
def test_add_new_contact(app, contact):
    old_contact_list = app.contact.get_contact_list()
    # infoclass = Info("USA", "406214", "My notes about work", "с@test.ru", "a@test.ru", "b@test.ru", "01-01-01", "02-02-02", "03-04-05", "06-07-08", "MyTitle", "MyCompany", "Russia", "Petrov", "Petr", "Petrovich", "Petya")
    app.contact.create_contact(contact)
    assert len(old_contact_list) + 1 == app.contact.count_of_contact()
    new_contact_list = app.contact.get_contact_list()
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Info.id_or_max) == sorted(new_contact_list, key=Info.id_or_max)
