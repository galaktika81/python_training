# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
from generator.random import random_string

def test_remove_contact_from_group(app, db):
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
    oldGroupContacts.sort(key=Contact.id_or_max)
    newGroupContacts.sort(key=Contact.id_or_max)
    assert oldGroupContacts== newGroupContacts
    id = newGroupContacts[-1].id
    app.contact.delete_by_id(id)
    oldGroupContacts.remove(contact)
    newGroupContacts = db.get_contacts_in_group(group)
    assert len(oldGroupContacts) == len(newGroupContacts)
    newGroupContacts.sort(key=Contact.id_or_max)
    assert oldGroupContacts== newGroupContacts
