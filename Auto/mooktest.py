#usr/bin/python
#encoding:utf-8
import time
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
desired_caps['appPackage'] = 'com.android.mms'
desired_caps['appActivity'] = '.ui.ConversationList'
desired_caps["unicodeKeyboard"] = "True"
desired_caps["resetKeyboard"] = "True"
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_id("action_compose_new").click()
time.sleep(1)
driver.find_element_by_id("recipients_editor").send_keys("18565687532")
driver.find_element_by_id("embedded_text_editor").send_keys("mooktest")
driver.find_element_by_id("send_button_sms").click()

try:
    if driver.find_element_by_id("recipients_editor").is_displayed():
        print("fail")
except Exception as e:
        print(e)
        print("pass")

driver.quit()

time.sleep(5)