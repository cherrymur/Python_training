from group import Group
from application import Application# group.py - package group, Group - module
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture)
    return fixture

def test_add_group(app):
    app.login(username="admin",
                   password="secret")  # don't change because these fields will not changed(almost 100% only 2 parametrs)
    app.create_group(Group(name="training", header="training", footer="training"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()