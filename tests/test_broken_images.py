#!/usr/bin/env python3

from config.test_settings import Page as page
from config.test_settings import Settings as site_settings
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import requests

# Test we can open the page and the header says "Broken Images"
def test_elements_page_heading(browser, broken_images_page):
    browser.get(broken_images_page)
    assert browser.find_element(By.XPATH, '/html/body/div[2]/div/div/h3').text == "Broken Images"

# Test to see if the pictures on the page load
def test_images_work(browser, broken_images_page):
    browser.get(broken_images_page)
    # Find all images
    images = browser.find_elements(By.TAG_NAME, "img")
    # Store all the images in a list
    image_urls = []
    for image in images:
        """
        Get the image path:
        IE: https://the-internet.herokuapp.com/asdf.jpg
        """
        image_urls.append(image.get_property("src"))
    # Check the response codes to see if we can load the images 404 = bad
    for image_url in image_urls:
        x = requests.get(image_url)
        if x.status_code == 404:
            assert False, "%s returned with %s" % (image_url, str(x.status_code))
