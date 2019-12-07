#Create common fixture
from fixture.application import Application# group.py - package group, Group - module
import pytest

fixture = None

@pytest.fixture #we check before each test, that browser is ok
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.login(username="admin",
                  password="secret")  # don't change because these fields will not changed(almost 100% only 2 parametrs)
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.login(username="admin", password="secret")
    return fixture

@pytest.fixture(scope="session",autouse=True)  # make all test in one launch of test
def stop(request):
    def fin():
        fixture.session.logout()  # fixture is the same as app. in other files
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture