# Create common fixture
from fixture.application import Application  # group.py - package group, Group - module
import pytest
import json

fixture = None
target = None

# intialization fixture before each test
@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        with open(request.config.getoption("--target")) as config_file:
            target = json.load(config_file)
    if fixture is None or not fixture.is_valid():  # check that fixture not exists
        fixture = Application(browser=browser, baseUrl=target['baseUrl'])
    fixture.session.ensure_login(username=target['username'], password=target['password'])  # make it ones for all tests
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