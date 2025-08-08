import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture()
def browser():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    yield driver
    driver.quit()

def test_open_s6(browser):
    browser.get("https://skillbox.ru")
    assert "Skillbox" in browser.title