import pytest
from pageobject import Page
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(2)

    pytest.page = Page(driver, "https://github.com/")

    try:
        yield driver
    finally:
        driver.quit()
    return driver
