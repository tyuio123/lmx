import unittest
import requests


class TestCaiPu(unittest.TestCase):
    def test_zhengque(self): #这里测试菜谱完全正确
        url = "http://apis.juhe.cn/cook/query"
        can = {
              "key": "07033c82bea1f71a0b2fc3e401777439",
              "menu": u"白菜"
            }

        r = requests.post(url, data=can)
        print(r.status_code)
        print(r.text)

        #因为返回是json格式，所以使用json进行验证

        refan = r.json()["reason"]  #这里返回的reason如果成功，name应该是"Success"
        print(refan)

        #断言
        self.assertEqual("Success", refan, msg="不好意思，失败了")



if __name__ == "__main__":
    unittest.main()

