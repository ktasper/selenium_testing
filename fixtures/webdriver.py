import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def browser():
    browser = webdriver.Firefox()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()

