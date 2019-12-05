#Create common fixture
from fixture.application import Application# group.py - package group, Group - module
import pytest

@pytest.fixture(scope="session") #make all test in one launch of test
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture