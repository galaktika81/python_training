__author__ = 'galyna'

import pytest
from fixture.application import Application


fixture = None


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    login = request.config.getoption("--login")
    password = request.config.getoption("--password")
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url)
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_url=base_url)
    fixture.session.ensure_login(username=login, password=password )
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def finalizer():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(finalizer)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")
    parser.addoption("--login", action="store", default="admin")
    parser.addoption("--password", action="store", default="secret")