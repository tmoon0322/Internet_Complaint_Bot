from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 100
PROMISED_UP = 50
TWITTER_EMAIL = "twinsmoon0322@gmail.com"
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 1
        self.down = 1

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)
        start_button = self.driver.find_element(by="xpath", value='//*[@id="container"]/div/div[3]'
                                                                  '/div/div/div/div[2]/div[3]/div[1]/a')
        start_button.click()
        time.sleep(40)
        self.down = float(self.driver.find_element(by="xpath", value='//*[@id="container"]/div/'
                                                                    'div[3]/div/div/div/div[2]/div[3]/div'
                                                                    '[3]/div/div[3]'
                                                                    '/div/div/div[2]'
                                                                    '/div[1]/div[1]/div/div[2]/span').text)
        self.up = float(self.driver.find_element(by="xpath", value='//*[@id="container"]/div/div[3]/'
                                                                  'div/div/div/div[2]/div'
                                                                  '[3]/div[3]/div/div[3]/div/div/div'
                                                                  '[2]/div[1]/div[2]/div/div[2]/span').text)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(2)
        email_input = self.driver.find_element(by="xpath", value='/html/body/div/div/div/div[1]/div/div/div'
                                                                 '/div/div/div/div[2]/div[2]/div/div/div[2]/'
                                                                 'div[2]/div/div/div/div[5]/label/div/div[2]/'
                                                                 'div/input')
        email_input.send_keys(TWITTER_EMAIL)
        email_input.send_keys(Keys.ENTER)
        time.sleep(3)
        user_input = self.driver.find_element(by="xpath", value='/html/body/div/div/div/div[1]/div/div/div/div/div/div'
                                                                '/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]'
                                                                '/label/div/div[2]/div/input')
        user_input.send_keys("tmoon0322", Keys.ENTER)
        time.sleep(2)
        password_input = self.driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div[2]'
                                                                    '/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div'
                                                                    '[3]/div/label/div/div[2]/div[1]/input')
        password_input.send_keys(TWITTER_PASSWORD)
        password_input.send_keys(Keys.ENTER)
        time.sleep(4)
        post_button = self.driver.find_element(by="xpath", value='//*[@id="react-root"]/div/div/div[2]/header/div/div/'
                                                                 'div/div[1]/div[3]/a')
        post_button.click()
        time.sleep(2)
        post_contents = self.driver.find_element(by="xpath", value='//*[@id="layers"]/div[2]/div/div/div/div/div/'
                                                                   'div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/'
                                                                   'div/div/div/div[1]/div[2]/div/div/div/div/div/'
                                                                   'div/div[2]/div/div/div/div/label/div[1]/div/div'
                                                                   '/div/div/div/div[2]/div')
        post_contents.send_keys(f"Hey ISP, why are these my speeds: download: {self.down} upload: {self.up}, when I was"
                                f" promised download: {PROMISED_DOWN} upload: {PROMISED_UP}")
        time.sleep(3)
        post_button = self.driver.find_element(by="xpath", value='//*[@id="layers"]/div[2]/div/div/div/div/div/'
                                                                 'div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]'
                                                                 '/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]')
        post_button.click()

        input()


complaint_bot = InternetSpeedTwitterBot()


complaint_bot.get_internet_speed()
if PROMISED_DOWN > complaint_bot.down or PROMISED_UP > complaint_bot.up:
    complaint_bot.tweet_at_provider()
