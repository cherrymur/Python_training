# Create common fixture
from fixture.application import Application  # group.py - package group, Group - module
import json
import os.path
import pytest
import importlib


fixture = None
target = None

# intialization fixture before each test
@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:
            target = json.load(f)
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


# takes .py file from data.package
def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_form_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_form_module(module):
    return importlib.import_module("data.%s" % module).testdata