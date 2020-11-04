class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_new(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def back_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()