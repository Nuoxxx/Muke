#usr/bin/python
#encoding:utf-8
import time
from appium import webdriver
import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        desired_caps['appPackage'] = 'com.android.mms'
        desired_caps['appActivity'] = '.ui.ConversationList'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_something(self):
        # 新建短信
        self.driver.find_element_by_id("action_compose_new").click()
        # 联系人号码
        self.driver.find_element_by_id("recipients_editor").send_keys("1000000")
        # 短信内容
        self.driver.find_element_by_id("embedded_text_editor").send_keys("mooktest")
        # 发送短信
        self.driver.find_element_by_id("send_button_sms").click()
        exist = False
        try:
            if self.driver.find_element_by_id("recipients_editor").is_displayed():
                exist = True
        except :
            exist = False
        self.assertEqual(exist, False)

    def test_other(self):
        print("test other")
        self.assertEqual(True, True)
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
