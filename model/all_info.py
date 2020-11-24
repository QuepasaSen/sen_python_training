from sys import maxsize

class Info:

    def __init__(self, dop_address=None, dop_phone=None, notes=None, email=None, email2=None, email3=None, domashniy=None, mobilniy=None, rabochiy=None, fax=None, title=None, company=None, address=None, firstname=None, middlename=None, lastname=None, nickname=None,  all_phones_from_homepage=None, id=None):
        self.dop_address = dop_address
        self.dop_phone = dop_phone
        self.notes = notes
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.domashniy = domashniy
        self.mobilniy = mobilniy
        self.rabochiy = rabochiy
        self.fax = fax
        self.title = title
        self.company = company
        self.address = address
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.all_phones_from_homepage = all_phones_from_homepage
        self.id = id

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def __repr__(self):
        return "%s,%s,%s" % (self.firstname, self.lastname, self.id)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize