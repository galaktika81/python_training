__author__ = 'galyna'
from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_first(Contact("hjkiuy", "bnmjhgfd", "fdcvbnhgf"))
