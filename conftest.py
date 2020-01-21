# Create common fixture
from fixture.application import Application  # group.py - package group, Group - module
import pytest

fixture = None

# intialization fixture before each test
@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    baseUrl = request.config.getoption("--baseUrl")
    if fixture is None:  # check that fixture not exists
        fixture = Application(browser=browser, baseUrl=baseUrl)
    else:
        if not fixture.is_valid():  # create new fixture, if now it's no valid
            fixture = Application(browser=browser, baseUrl=baseUrl)
    fixture.session.ensure_login(username="admin", password="secret")  # make it ones for all tests
    return fixture

# finalization fixture(logout and close browser)
@pytest.fixture(scope="session", autouse=True)  # make all tests in one launch of test and automatic
def stop(request):
    def fin():  # one logout for all tests
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")