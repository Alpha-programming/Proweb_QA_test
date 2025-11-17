import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import shutil

@pytest.fixture(params=["edge", "chrome", "firefox"])
def driver(request):
    browser = request.param

    # if browser == "edge" and not shutil.which("msedgedriver"):
    #     pytest.skip("Edge WebDriver not found, skipping Edge tests")
    # if browser == "chrome" and not shutil.which("chromedriver"):
    #     pytest.skip("Chrome WebDriver not found, skipping Chrome tests")
    if browser == "firefox" and not shutil.which("geckodriver"):
        pytest.skip("Firefox WebDriver not found, skipping Firefox tests")

    # if browser == "edge":
    #     driver = webdriver.Edge()
    # elif browser == "chrome":
    #     driver = webdriver.Chrome()
    if browser == "firefox":
        driver = webdriver.Firefox()

    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
