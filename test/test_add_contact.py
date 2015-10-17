# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata= [Contact(firstname="", middlename="", lastname="")] + [
   Contact(firstname=random_string("fname", 15), middlename=random_string("mname", 15), lastname=random_string("lname", 15))
    for i in range(5)
]

# testdata= [
#    Group(name=name, header=header, footer=footer)
#     for name in ["", random_string("fname", 15)]
#     for header in ["", random_string("mname", 15)]
#     for footer in ["", random_string("lname", 15)]
# ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
