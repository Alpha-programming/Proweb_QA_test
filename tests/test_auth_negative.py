# import pytest
# import time
# from pages.auth_page import AuthPage
# from selenium.common.exceptions import TimeoutException
#
# def test_login_negative(driver):
#     driver.get("https://my.proweb.uz/home")
#     auth_page = AuthPage(driver)
#     auth_page.input_login("999999999999")
#     auth_page.click_button_next()
#     try:
#         auth_page.input_password("wrongpassword")
#         auth_page.click_button_submit()
#         time.sleep(2)
#         assert "error" in driver.page_source.lower() or "невер" in driver.page_source.lower()
#     except TimeoutException:
#         assert True