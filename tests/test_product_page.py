import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_product_list_visible(browser):
    login = LoginPage(browser)
    login.load()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(browser)
    products = inventory.get_product_titles()
    assert len(products) > 0
