from Base.helper import Helper
from selenium import webdriver
#from Base.common_func import *
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy

class WelcomePage(Helper):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)

    def click_login_btn(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "welcome_screen_sign_in_button").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '계속').click()

