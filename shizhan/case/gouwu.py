import unittest
import requests



class TestGouwu(unittest.TestCase):
    def zhuce(self):
        url = "http://localhost:8080/test/mem.do"
        head = {
           "Proxy - Connection": "keep - alive",
           "Content - Length": "143",
           "Cache - Control": "max - age = 0",
           "Origin": "http: // localhost: 8080",
           "Upgrade - Insecure - Requests": "1",
           "User - Agent": "Mozilla/5.0(Windows NT 6.1;WOW64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/55.0.2883.87Safari/537.36",
           "Content - Type": "application / x - www - form - urlencoded",
           "Accept": "text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, * / *;q = 0.8",
           "Referer": "http: // localhost: 8080 / test / reg.jsp",
           "Accept - Encoding": "gzip, deflate, br",
           "Accept - Language": "zh - CN, zh;q = 0.8",
           "Cookie": "JSESSIONID = E03B2CE9922433C32090BAA2773ADAC1;.1532484034878 .353;monitor_count = 48",
              }
        can = {
           "method": "reg",
           "memberlevel": "4",
           "memberName": "ww",
           "loginName": "ww",
           "loginPwd": "ww",
           "phone": "15116425789",
           "address": u"中国各地",
           "zip": "119110",
           "email": u"qwe@qq.com",
           "C_Input": u"注册"
              }
        r = requests.post(url,headers=head,data=can)
        print(r.status_code)
        print(r.text)



"""
    def denglu(self):
      url = "http://localhost:8080/test/Admin/login.do?method=login"
      head = {
            "Proxy-Connection": "keep-alive",
            "Content-Length": "42",
            "Cache-Control": "max-age=0",
            "Origin": "http://localhost:8080",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Referer": "http://localhost:8080/test/Admin/adminLogin.jsp",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Cookie": "JSESSIONID=A3191ED3F0A4784218E0394B62FB02C4; menu-AdminMenu=block; __guid=111872281.1120930517490028400.1532484034878.353; monitor_count=31"
             }
      can = {
            "method": "login",
            "loginName": "admin1",
            "loginPwd": "admin1",
            "x": "37",
            "y": "12"
             }
      r = requests.post(url,headers=head,data=can)
      print(r.status_code)
      print(r.text)

    def guanli(self):
      url = "http://localhost:8080/test/Admin/adminMer.do"
      head = {
          "Proxy-Connection": "keep-alive",
          "Upgrade-Insecure-Requests": "1",
          "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
          "Referer": "http://localhost:8080/test/adminMenu.jsp",
          "Accept-Encoding": "gzip, deflate, sdch, br",
          "Accept-Language": "zh-CN,zh;q=0.8",
          "Cookie": "JSESSIONID=A3191ED3F0A4784218E0394B62FB02C4; menu-AdminMenu=block; __guid=111872281.1120930517490028400.1532484034878.353; monitor_count=32"
             }
      can = {
            "method": "browseMer",
             }
      r = requests.post(url,headers=head,data=can)
      print(r.status_code)
      print(r.text)
    def tianjia(self):
      url = "http://localhost:8080/test/Admin/adminAddMer.jsp"
      head = {
          "Proxy-Connection": "keep-alive",
          "Upgrade-Insecure-Requests": "1",
          "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
          "Referer": "http://localhost:8080/test/adminMenu.jsp",
          "Accept-Encoding": "gzip, deflate, sdch, br",
          "Accept-Language": "zh-CN,zh;q=0.8",
          "Cookie": "JSESSIONID=A3191ED3F0A4784218E0394B62FB02C4; menu-AdminMenu=block; __guid=111872281.1120930517490028400.1532484034878.353; monitor_count=32"
             }
      can = {
            "method": "browseMer",
             }
      r = requests.post(url,headers=head,data=can)
      print(r.status_code)
      print(r.text)
 """







