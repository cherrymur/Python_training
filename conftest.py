#Create common fixture
from fixture.application import Application# group.py - package group, Group - module
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture