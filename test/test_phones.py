import re

def test_phones_on_homepage(app):
    contact_from_homepage = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_homepage.domashniy == clear(contact_from_edit_page.domashniy)
    assert contact_from_homepage.mobilniy == clear(contact_from_edit_page.mobilniy)
    assert contact_from_homepage.rabochiy == clear(contact_from_edit_page.rabochiy)
    assert contact_from_homepage.dop_phone == clear(contact_from_edit_page.dop_phone)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.domashniy == contact_from_edit_page.domashniy
    assert contact_from_view_page.mobilniy == contact_from_edit_page.mobilniy
    assert contact_from_view_page.rabochiy == contact_from_edit_page.rabochiy
    assert contact_from_view_page.dop_phone == contact_from_edit_page.dop_phone

def clear(s):
    return re.sub("[() -]","", s)