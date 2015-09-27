__author__ = 'galyna'


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first()
    app.session.logout()
