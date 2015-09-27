__author__ = 'galyna'
from model.contact import Contact

def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first(Contact("hjkiuy", "bnmjhgfd", "fdcvbnhgf"))
    app.session.logout()