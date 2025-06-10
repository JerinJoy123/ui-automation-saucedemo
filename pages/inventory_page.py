from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def get_product_titles(self):
        return self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
