__author__ = 'galyna'
from model.group import Group


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group("ghjjk", "vbnm", "sdewq"))
    app.session.logout()
