import pytest
from config.test_settings import Page as page
from config.test_settings import Settings as site_settings
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope='session')
def add_remove_elements_button_xpath():
    xpath = '/html/body/div[2]/div/div/button'
    yield xpath


# Test we can open the page and the header says "Add/Remove Elements"
def test_elements_page_heading(browser, add_remove_elements_page):
    browser.get(add_remove_elements_page)
    assert browser.find_element(By.XPATH, '//*[@id="content"]/h3').text == "Add/Remove Elements"

# Test when we click "Add Element" a new element is created
## Before we do that we need to test to see if the button exists.
def test_element_button_exists(browser, add_remove_elements_page, add_remove_elements_button_xpath):
    browser.get(add_remove_elements_page)
    assert browser.find_element(By.XPATH, add_remove_elements_button_xpath).text == "Add Element"
## Now that we are testing the button exists we can click it

def test_element_button(browser, add_remove_elements_page, add_remove_elements_button_xpath):
    browser.get(add_remove_elements_page)
    # Click the button 2 times
    for _ in range (0, 2):
        browser.find_element(By.XPATH, add_remove_elements_button_xpath).click()
        time.sleep(1)
    # Check its spawned 2 buttons with the words "Delete" on them
    assert browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/button').text == "Delete"
    assert browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/button[2]').text == "Delete"

# Test we can delete the new element
def test_element_spwaned_button_delete(browser, add_remove_elements_page, add_remove_elements_button_xpath):
    browser.get(add_remove_elements_page)
    # Click the button
    browser.find_element(By.XPATH, add_remove_elements_button_xpath).click()
    # Click the spwaned button to delete it
    #browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/button').click()
    try:
        assert browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/button').text == NoSuchElementException
        assert False, "Button still exists"
    # If the button does not exist it means we delete it so we can pass this test
    except NoSuchElementException:
        assert True
