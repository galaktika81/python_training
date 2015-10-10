__author__ = 'galyna'
from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))

    old_contacts = app.contact.get_contact_list()
    contact = Contact("hjkiuy", "bnmjhgfd", "fdcvbnhgf")
    contact.id = old_contacts[0].id
    app.contact.modify_first(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_modify_contact_first_name(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="test"))
#     app.contact.modify_first(Contact(firstname="gfdggfd"))