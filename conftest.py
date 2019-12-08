#Create common fixture
from fixture.application import Application # group.py - package group, Group - module
import pytest

@pytest.fixture(scope="session") #make all test in one launch of test
def app(request):
    fixture = Application()
    fixture.session.login(username="admin", password="secret") #added to make it ones
    def fin(): #added one logout for each test
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture