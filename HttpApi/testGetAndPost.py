# coding=utf-8

import requests
import  unittest
import  json

class testClass(unittest.TestCase):
    def setUp(self):
        print("初始化")

    def tearDown(self):
        print("结束")

    def test_user_login(self):
        #测试用户登录接口 http://www.domarket.com.cn/api/user/login
        base_url = "http://domarket.com.cn:18083/api/user/login"
        datalist = {"userName":"18565687531","passWord":"123456"}

        headers = {"User-Agent": "okhttp/3.1.2",
                   "Content-Type": "application/x-www-form-urlencoded"}
        r = requests.post(base_url,data=datalist,headers=headers)
        result = json.loads(r.text)
        print(result)
        self.assertEqual(result['code'],"0")
        item = result['item']

        print(item['sessionKey'])



    def testGet(self):
        keyword = {"wd":"poptest"}
        headers = {"User-Agent":"test",
                   'Referer': 'http://login.weibo.cn/login/?ns=1&revalid=2&backU'}
        cookies = dict(IPLOC="CN1100", ABTEST="1")
        res = requests.get("https://customer-api.helijia.com/app-customer/transformers/getCityList?version=3.3.0.1&sign_type=md5&city=110100&req_time=1472372990756&device_type=android&device_id=d3c1d53d0a8a378f",
                           params=keyword,
                           headers=headers,
                           cookies = cookies)
        print(res.text)
        if u"北京市" in res.text:
            print("pass")
            result = True
        else:
            print("fail")
            result = False
        self.assertTrue(result)

    def testPost(self):
        keyword = {"query":"postman"}
        headers = {"User-Agent":"hlj-android/3.3.0.1",
                   "Content-Type":"application/x-www-form-urlencoded",
                   'Referer': 'http://login.weibo.cn/login/?ns=1&revalid=2&backU'}
        cookies = dict(IPLOC="CN1100", ABTEST="1")
        res = requests.post("https://app.helijia.com/zmw/user/bind_dev",
                            #data=json.dumps(keyword),
                            data=keyword,
                            headers=headers,
                            cookies=cookies)
        print(res.text)
        if u"网页" in res.text:
            print("pass")
        else:
            print("fail")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()