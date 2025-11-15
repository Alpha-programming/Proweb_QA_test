from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time

class CommentPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.choose_homework = (By.CSS_SELECTOR,
            '#app > div > div.home-content > div > div > div > div > div.home__education > div.home__education-homework.home__education-homework-works > div.tab-content.home__homeworks-tabview > div > div.home__works > div > div > div:nth-child(3) > div.avatar.baseavatar.baseavatar_go.baseavatar-small.home__homework-go')
        self.comment_input = (By.CSS_SELECTOR,
            '#app > div > div.container.homework-page-container > div > div > div > div.solved-homework__materials > div.message-input.relative.solved-homework-input > div > div > label > textarea')
        self.comment_send = (By.CSS_SELECTOR,
            '#app > div > div.container.homework-page-container > div > div > div > div.solved-homework__materials > div.message-input.relative.solved-homework-input > button')

    def choose_homework_btn(self):
        try:
            element = self.wait.until(EC.element_to_be_clickable(self.choose_homework))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            ActionChains(self.driver).move_to_element(element).click().perform()
        except ElementClickInterceptedException:
            time.sleep(1)
            element = self.wait.until(EC.element_to_be_clickable(self.choose_homework))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            ActionChains(self.driver).move_to_element(element).click().perform()

    def comment_input_def(self, text='Test'):
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.comment_input))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            print("Поле комментария не найдено!")

    def send_comment_btn(self):
        try:
            element = self.wait.until(EC.element_to_be_clickable(self.comment_send))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            ActionChains(self.driver).move_to_element(element).click().perform()
        except TimeoutException:
            print("Кнопка отправки комментария не найдена!")

    def write_send_comment(self, text='Test'):
        self.choose_homework_btn()
        self.comment_input_def(text)
        self.send_comment_btn()
        time.sleep(5)

