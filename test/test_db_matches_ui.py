from model.group import Group
from timeit import timeit


def test_group_list(app, db):
    print(timeit(lambda: app.group.get_group_list(), number=1))
    print(timeit(lambda: db.get_group_list(), number=1000))
    assert False # sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
