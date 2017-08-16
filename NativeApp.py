import unittest
from appium import  webdriver

class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.Settings'
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

    # def test_otherAPI(self):
    #
    #     self.assertEqual(True, False)

    def test_MoreAPIs(self):
        els = self.driver.find_elements_by_class_name()

    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()
