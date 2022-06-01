#!/usr/bin/env python3
import pytest
from config.test_settings import Page as page

# Loads the add_remove_elements page
@pytest.fixture(scope='session')
def add_remove_elements_page():
    yield page.elements

@pytest.fixture(scope='session')
def broken_images_page():
    yield page.broken_images
