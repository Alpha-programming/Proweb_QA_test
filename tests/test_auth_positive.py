import pytest
import time
from selenium.common.exceptions import TimeoutException
from pages.auth_page import AuthPage
from pages.base_page import BasePage
from pages.comment_page import CommentPage

def test_auth_chrome(driver):
    driver.get('https://my.proweb.uz/home')
    auth_page = AuthPage(driver)
    auth_page.input_login('820105802172')
    auth_page.click_button_next()
    auth_page.input_password('Alpha2005@')
    auth_page.click_button_submit()
    try:
        auth_page.click_button_sessions()
        auth_page.click_button_finish()
    except:
        pass
    # base_page = BasePage(driver)
    # base_page.play_and_evaluate_exit()

    comment_page = CommentPage(driver)
    comment_page.write_send_comment()