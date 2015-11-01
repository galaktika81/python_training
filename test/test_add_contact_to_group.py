# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
from generator.random import random_string

def test_add_contact_to_group(app, db):
    groups = db.get_group_list()
    if len(groups) is 0:
        app.group.create(Group(name='GroupForContacts'))
        groups = db.get_group_list()

    group = groups[0]
    oldGroupContacts = db.get_contacts_in_group(group)
    contact = Contact(firstname=random_string('ContactForGroup', 3),  lastname=random_string('ln', 3), group=group)
    app.contact.create(contact)
    newGroupContacts = db.get_contacts_in_group(group)
    oldGroupContacts.append(contact)
    assert len(oldGroupContacts) == len(newGroupContacts)
    assert sorted(oldGroupContacts, key=Contact.id_or_max) == sorted(newGroupContacts, key=Contact.id_or_max)

