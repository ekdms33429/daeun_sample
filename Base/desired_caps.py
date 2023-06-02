import os
from typing import Any, Dict

BUNDLE_ID = 'com.nike.omega'
SERVER_URL = 'http://127.0.0.1:4723'
#SERVER_URL = 'http://127.0.0.1:4723/wd/hub'
APP_PATH = None
# app = os.path.join(os.path.dirname(__file__), '/Users/daeunkim/File/ipk/.ipa')
# app = os.path.abspath(app)

def PATH(p: str) -> str:
    return os.path.abspath(os.path.join(os.path.dirname(__file__), p))

#input data
data_set = {
    "김다은": {
        "name": "김다은",
        "pw": "Qawsedrf1!",
        "email": "ekdms33429@gmail.com",
        "birth": "1997년 8월 18일",
    }
}

#device info
desired_caps: Dict[str, Any] = {
    "ios_14pro": {
      "platformName": "iOS",
      "appium:platformVersion": "16.4",
      "appium:automationName": "XCUITest",
      "appium:deviceName": "iPhone 14 Pro",
      "appium:udid": "00008120-000A404A34E0C01E"
    }
}

#set desired_capability
def get_desired_caps(device) -> Dict[str, Any]:
    desired_cap = desired_caps[device]

    # 파일 지정 시
    if APP_PATH is not None:
        desired_cap['app'] = PATH(os.path.join('../../..', 'apps', APP_PATH))
    # 없을 시 BUNDLE_ID 입력
    else:
        desired_cap['bundleId'] = BUNDLE_ID

    return desired_cap

#set input data
def get_input_data(name) -> Dict[str, Any]:
    my_data = data_set[name]
    return my_data





