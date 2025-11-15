from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException,ElementClickInterceptedException

class AuthPage:
    def __init__(self, driver):
        self.driver = driver
        self.login = (By.CSS_SELECTOR, '#app > div > div > div > div.log-in__container > div > div.log-in__newContent-right > div > div.log-in__newContent-right-block-wrap > form > div.log-in__newContent-right-block-center > div > label > input')
        self.btn_next = (By.CSS_SELECTOR, '#app > div > div > div > div.log-in__container > div > div.log-in__newContent-right > div > div.log-in__newContent-right-block-wrap > form > div.log-in__newContent-right-block-bot > button')
        self.password = (By.CSS_SELECTOR, '#app > div > div > div > div.log-in__container > div > div.log-in__newContent-right > div > div.log-in__newContent-right-block-wrap > form > div.log-in__newContent-right-block-center.log-in__newContent-right-block-center-checkpass > div.log-in__newContent-right-block-center-inp > label > input')
        self.btn_submit = (By.CSS_SELECTOR, '#app > div > div > div > div.log-in__container > div > div.log-in__newContent-right > div > div.log-in__newContent-right-block-wrap > form > div.log-in__newContent-right-block-bot > button')
        self.btn_sessions = (By.CSS_SELECTOR, 'div.drop-down-component:nth-child(4) > div:nth-child(1) > div:nth-child(1)')
        self.btn_finish = (By.CSS_SELECTOR, '#dialog > div > div > div > div.material-dialog__window-body.material-dialog__window-body_modify > div > div:nth-child(4) > div.drop-down-component__content > div.sessions__item-content > button')

    def input_login(self, login):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located(self.login)).send_keys(login)

    def click_button_next(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.element_to_be_clickable(self.btn_next)).click()

    def input_password(self, password):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located(self.password)).send_keys(password)

    def click_button_submit(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.element_to_be_clickable(self.btn_submit)).click()

    def click_button_sessions(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.element_to_be_clickable(self.btn_sessions)).click()

    def click_button_finish(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.element_to_be_clickable(self.btn_finish)).click()

