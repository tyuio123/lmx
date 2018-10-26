import unittest
import requests


class TestTianqi(unittest.TestCase):
    def test_tianqi(self):
      url = "http://v.juhe.cn/historyWeather/province"
      cans = {
        "Key": "4a401d3667bb7563c082ff37137acc35",
        "province": u"北京"
             }
      q = requests.get(url ,json=cans)
      print(q.status_code)
      print(q.text)























