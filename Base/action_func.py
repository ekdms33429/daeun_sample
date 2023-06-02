import time

# UI 동작 관련
def click_element_scrolled_into_view(self, element):
    #  element display 여부 -> false면 scroll to element -> click element(using location)
    loc = element.location
    if element.is_displayed() == False:
        self.driver.execute_script('mobile: scroll', {"element": element, "toVisible": True})
    self.driver.tap([(int(loc['x']), int(loc['y']))])
    time.sleep(0.5)
