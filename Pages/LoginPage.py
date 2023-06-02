import time
from Base.helper import Helper
from appium.webdriver.common.appiumby import AppiumBy
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import NoSuchElementException
from Base.check_func import CheckFunc

class LoginPage(Helper):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)
        self.check = CheckFunc()
        self.terms = ['위 주문의 상품, 가격, 할인, 배송정보에 동의합니다', '개인 정보 수집 및 이용에 동의합니다', '개인 정보의 제3자 제공 및 국외 이전 에 동의합니다']

    #이메일 입력
    def enter_email(self):
        exp_region = '대한민국'
        exp_url = '‎accounts.nike.com, 보안 확인됨'
        try:
            act_url = self.driver.find_elements(AppiumBy.NAME, "URL")[0].get_attribute('value')
            act_region = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "국가 변경").get_attribute('value')
            self.check.check_equal(exp_region, act_region, soft_check=True)
            self.check.check_equal(exp_url, act_url)
            self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,'**/XCUIElementTypeOther[`label == "나이키에 오신 것을 환영합니다 - 로그인"`]/XCUIElementTypeOther/XCUIElementTypeTextField')\
                .send_keys(self.driver.data_set['email']).send_keys(webdriver.Keys.ENTER)
        except NoSuchElementException:
            self.check.logger.error("We can't find the element :( ")
            return False


    #전체 약관 동의
    def agree_all_terms(self):
        try:
            self. driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSwitch[`label == "모든 약관에 동의합니다"`]').click()
            for name in self.terms:
                item = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, name)
                if item.get_attribute('value') == '1':
                    pass
                else:
                    self.check.logger.error("all terms btn error")
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '계속').click()
        except NoSuchElementException:
            self.check.logger.error("We can't find the element :( ")
            return False

    #일부 약관 동의 -> 전체 동의
    def agree_some_terms(self):
        from random import randint
        from Base.action_func import click_element_scrolled_into_view

        try:
            # 임의의 정수
            rand = randint(0, 2)
            self. driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSwitch[`label == "모든 약관에 동의합니다"`]').click()
            for i, name in enumerate(self.terms):
                item = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, name)
                if i == rand:
                    # 일부 버튼 미동의 처리
                    item.is_displayed()
                    click_element_scrolled_into_view(self, item)
                elif item.get_attribute('value') == '1':
                    pass
                else:
                    self.check.logger.error("all terms btn error")
            btn_next = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '계속')
            click_element_scrolled_into_view(self, btn_next)
            # 필수 미동의 안내 문구 노출
            err_msg = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '오류: 계속하려면 모든 확인란을 선택해야 합니다.')
            if not err_msg.is_displayed():
                self.check.logger.error("Error message not exposed")
                return False
            # 잔여 버튼 동의 처리
            btn_off = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.terms[rand])
            click_element_scrolled_into_view(self, btn_off)
            click_element_scrolled_into_view(self, btn_next)
        except NoSuchElementException:
            self.check.logger.error("We can't find the element :( ")
            return False

    # 비밀번호 입력
    def enter_pw(self):
        try:
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.driver.data_set['email'])
            self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`label == "나이키에 오신 것을 환영합니다 - 로그인"`]/XCUIElementTypeOther/XCUIElementTypeSecureTextField')\
                .send_keys(self.driver.data_set['pw']).send_keys(webdriver.Keys.ENTER)
            self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "로그인되었습니다."`]')
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '계속').click()
        except NoSuchElementException:
            self.check.logger.error("We can't find the element :( ")
            return False