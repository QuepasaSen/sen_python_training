def test_phones_on_homepage(app):
    contact_from_homepage = app.contact.get_contact_list()[0]
    contact_from_editpage = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_homepage.domashniy == contact_from_editpage.domashniy
    assert contact_from_homepage.mobilniy == contact_from_editpage.mobilniy
    assert contact_from_homepage.rabochiy == contact_from_editpage.rabochiy
    assert contact_from_homepage.dop_phone == contact_from_editpage.dop_phone