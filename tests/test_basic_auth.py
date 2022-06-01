#!/usr/bin/env python3
from config.test_settings import Page as page
from config.test_settings import Settings as site_settings
from selenium.webdriver.common.by import By

def test_basic_auth_login_success(browser):
    # https://user:pass@site.com
    url = site_settings.protocol_slug + "{}:{}@".format(site_settings.basic_auth_user, site_settings.basic_auth_password) + page.basic_auth
    # Check the p tag shows us "Congratulations!"
    browser.get(url)
    assert "Congratulations!" in browser.find_element(By.XPATH, '//*[@id="content"]/div/p').text

