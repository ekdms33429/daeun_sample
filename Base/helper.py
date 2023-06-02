import unittest
from appium import webdriver
from appium.options.ios import XCUITestOptions
from Base.desired_caps import *
#--------------------------------------------
DEVICE_NAME = "ios_14pro"
MY_NAME = "김다은"
#--------------------------------------------

class Helper(unittest.TestCase):
    def setUp(self):
        self.desired_cap = get_desired_caps(DEVICE_NAME)
        self.driver = webdriver.Remote(SERVER_URL, options=XCUITestOptions().load_capabilities(self.desired_cap))
        self.driver.implicitly_wait(7)
        self.driver.data_set = get_input_data(MY_NAME)

    def tearDown(self) -> None:  # type: ignore
        if not hasattr(self, 'driver'):
            return

        # 앱 종료
        #self.driver.terminate_app(BUNDLE_ID)

        # 앱 재진입
        # self.driver.quit()