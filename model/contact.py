from sys import maxsize


class Contact:
    # added None value to be able to change only one parametr
    def __init__(self, id=None, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, all_phones_from_home_page=None, all_phones_from_view_page=None, homephone=None, mobilephone=None, workphone=None, faxphone=None,
                 all_emails_from_home_page=None, all_emails_from_view_page=None, email=None, email2=None, email3=None, homepage=None, bday=None,
                 bmonth=None, byear=None, aday=None, amonth=None, ayear=None, address2=None, notes=None, secondaryphone=None):
        self.id = id
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.faxphone = faxphone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.notes = notes
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.all_phones_from_view_page = all_phones_from_view_page
        self.all_emails_from_view_page = all_emails_from_view_page

    def __repr__(self):
        return "%s:%s %s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname\
               and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
