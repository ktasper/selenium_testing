# Define site wide settings here:
class Settings:
    basic_auth_user = "admin"
    basic_auth_password = "admin"
    protocol = "https"
    protocol_slug = protocol + "://"

# Set up the page definitions here
class Page:
    page_url = 'the-internet.herokuapp.com'
    full_uri = Settings.protocol_slug + "{}".format(page_url)
    home = Settings.protocol_slug + "{}".format(page_url)
    basic_auth = page_url + "/basic_auth"
    elements = full_uri + "/add_remove_elements/"
    broken_images = full_uri + "/broken_images"
