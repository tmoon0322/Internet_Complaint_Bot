from selenium import webdriver


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 10
        self.down = 50

    def get_internet_speed(self):
