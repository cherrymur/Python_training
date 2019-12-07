#Create common fixture
from fixture.application import Application# group.py - package group, Group - module
import pytest

@pytest.fixture(scope="session") #make all test in one launch of test
def app(request):
    fixture = Application()
    fixture.session.login(username="admin",
                  password="secret")  # don't change because these fields will not changed(almost 100% only 2 parametrs)
    def fin():
        fixture.session.logout()  # fixture is the same as app. in other files
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture