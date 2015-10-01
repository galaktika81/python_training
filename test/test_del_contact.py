__author__ = 'galyna'


def test_del_contact(app):
    app.contact.delete_first()
