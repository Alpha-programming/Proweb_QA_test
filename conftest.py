import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["chrome", "firefox", "edge"])
def driver(request):
    browser = request.param

    # Detect if running in CI
    headless = os.getenv("CI") == "true"

    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        drv = webdriver.Chrome(
            ChromeDriverManager().install(),
            options=options
        )

    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        drv = webdriver.Firefox(
            executable_path=GeckoDriverManager().install(),
            options=options
        )

    elif browser == "edge":
        options = EdgeOptions()
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        drv = webdriver.Edge(
            EdgeChromiumDriverManager().install(),
            options=options
        )

    drv.implicitly_wait(10)
    yield drv
    drv.quit()

