__author__ = 'galyna'
from model.group import Group


def test_modify_group_name(app):
    app.group.modify_first(Group(name="New group"))


def test_modify_group_header(app):
    app.group.modify_first(Group(header="New header"))
