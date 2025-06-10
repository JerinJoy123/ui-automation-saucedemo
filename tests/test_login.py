import pytest
from pages.login_page import LoginPage

def test_valid_login(browser):
    login = LoginPage(browser)
    login.load()
    login.login("standard_user", "secret_sauce")
    assert "inventory" in browser.current_url
