import time
import requests
from Base.helper import Helper
from selenium import webdriver
import datetime

class ApiFunc(Helper):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def sample_api(self):
        timeout = 10
        # 번호로 탈퇴 처리
        stg_url = ""
        headers = {}
        ex_response = requests.get(stg_url, timeout=timeout)
        ex_response.raise_for_status()
        ex_result = ex_response.json()
        ex_id = ex_result[''][''][0]['']

