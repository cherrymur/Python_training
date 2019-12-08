# Create common fixture
from fixture.application import Application  # group.py - package group, Group - module
import pytest

fixture = None

# intialization fixture before each test
@pytest.fixture
def app(request):
    global fixture
    if fixture is None:  # check that fixture not exists
        fixture = Application()
        fixture.session.login(username="admin", password="secret")  # make it ones for all tests
    else:
        if not fixture.is_valid():  # create new fixture, if now it's no valid
            fixture = Application()
            fixture.session.login(username="admin", password="secret")  # make it ones for all tests
    return fixture

# finalization fixture(logout and close browser)
@pytest.fixture(scope="session", autouse=True)  # make all tests in one launch of test and automatic
def stop(request):
    def fin():  # one logout for all tests
        fixture.session.logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture
