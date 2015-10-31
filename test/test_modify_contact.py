__author__ = 'galyna'
from model.contact import Contact
import random

def test_modify_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    newContact = Contact("aaaaa", "bbb", "ccc")
    newContact.id = contact.id
    app.contact.modify_by_id(contact.id, newContact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()

    for i in range(len(old_contacts)):
        if old_contacts[i].id == newContact.id:
            old_contacts[i] = newContact

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

