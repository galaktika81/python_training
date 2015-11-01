__author__ = 'galyna'

from sys import maxsize

class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None,
                 id = None, address = None,
                 email = None, email2 = None, email3 = None, all_emails = None,
                 homephone = None, workphone = None, mobilephone = None, secondaryphone = None,
                 all_phones_from_home_page = None, group=None):

        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname

        self.id = id
        self.address = address

        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_emails = all_emails

        self.homephone = homephone
        self.workphone = workphone
        self.mobilephone = mobilephone
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page

        self.group = group

    def __repr__(self):
        return "%s;%s;%s;%s" % (self.id, self.firstname, self.middlename, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname \
               and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
