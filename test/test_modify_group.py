__author__ = 'galyna'
from model.group import Group
import random

def test_modify_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    newGroup = Group(name="New group")
    newGroup.id = group.id
    app.group.modify_group_by_id(group.id,newGroup)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()

    for i in range(len(old_groups)):
        if old_groups[i].id == newGroup.id:
            old_groups[i] = newGroup

    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)