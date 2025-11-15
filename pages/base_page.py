from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.click_course = (By.CSS_SELECTOR, '#app > div > div.home-content > div > div > div > div > div.home__education > div.home__education-page > div > div:nth-child(2) > div.home-card__bot > div > div.avatar.baseavatar_go.home-card__bot-content-btn.baseavatar')
        self.lessons_click = (By.CSS_SELECTOR, '#tabbar > div > div.tab-header > div.tab-header__wrapper > div:nth-child(2)')
        self.watch_click = (By.CSS_SELECTOR, '#app > div > div.container.container_mobile > div > div > div.new-lessons_content > div > div:nth-child(5) > div.flex.gap20 > div:nth-child(3) > div.lesson-card > div > div.lesson-card-left > div.lesson-card-left_actions > button > span')
        self.star_5 = (By.CSS_SELECTOR, '#app > div > div.videolesson > div > div:nth-child(2) > div > div.videolesson__general-footer-rating.mb10 > div > div > div > span:nth-child(5)')
        self.send_button = (By.CSS_SELECTOR, '#dialog > div > div > div > div > div > button')
        self.play_button = (By.CSS_SELECTOR, '#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(3) > div.video-player-proweb > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-left > button')
        self.btn_profile = (By.CSS_SELECTOR,"#app > div > div.header > div > div.header__avatar > div")
        self.btn_exit = (By.CSS_SELECTOR,"#app > div > div.inforation > div > div > div:nth-child(5)")
        self.btn_confirmation = (By.CSS_SELECTOR,"#dialog > div > div > div.material-dialog__window-actions > button:nth-child(2)")



    def click_course_button(self):
        self.wait.until(EC.element_to_be_clickable(self.click_course)).click()

    def click_lessons_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.lessons_click)).click()

    def click_watch_button(self):
        self.wait.until(EC.element_to_be_clickable(self.watch_click)).click()

    def play_video(self, duration=100):
        try:
            play_btn = self.wait.until(EC.element_to_be_clickable(self.play_button))
            play_btn.click()
            time.sleep(duration)
        except TimeoutException:
            pass

    def evaluate_lesson(self):
        try:
            star = self.wait.until(EC.element_to_be_clickable(self.star_5))
            star.click()
            send_btn = self.wait.until(EC.element_to_be_clickable(self.send_button))
            send_btn.click()
        except TimeoutException:
            pass

    def logout(self):
        try:
            profile = self.wait.until(EC.element_to_be_clickable(self.btn_profile))
            profile.click()
            exit_btn = self.wait.until(EC.element_to_be_clickable(self.btn_exit))
            exit_btn.click()
            confirm = self.wait.until(EC.element_to_be_clickable(self.btn_confirmation))
            confirm.click()
        except TimeoutException:
            pass

    def play_and_evaluate_exit(self):
        self.click_course_button()
        time.sleep(5)
        self.click_lessons_tab()
        self.click_watch_button()
        self.play_video(duration=100)
        self.evaluate_lesson()
        self.logout()


