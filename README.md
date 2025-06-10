#  UI Automation Framework for SauceDemo

This project automates functional UI tests for [saucedemo.com](https://www.saucedemo.com) using Python, Selenium, and Pytest. It follows the Page Object Model and integrates with GitHub Actions and Allure reporting.

##  Features
- Selenium WebDriver with WebDriver Manager
- Page Object Model structure
- Pytest test runner
- GitHub Actions CI
- Allure reporting

##  Running the Tests
```bash
pip install -r requirements.txt
pytest
allure serve reports/
```
