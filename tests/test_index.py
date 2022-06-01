from config.test_settings import Page as page

def test_title_loads(browser):
    browser.get(page.home)
    assert browser.title == 'The Internet'
