from Pages.WelcomePage import *
from Pages.LoginPage import *

class TestSample(Helper):
    def setUp(self):
        super().setUp()

    def test_login(self):
        welcome = WelcomePage(self.driver)
        login = LoginPage(self.driver)

        welcome.click_login_btn()
        login.enter_email()
        #약관 전체 동의
        #login.agree_all_terms()

        #약관 일부 동의
        login.agree_some_terms()
        login.enter_pw()

    def test_example(self):
        time.sleep(5)

if __name__ == '__main__':
    unittest.main(warnings='ignore')