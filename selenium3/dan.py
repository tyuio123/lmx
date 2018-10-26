
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time

class TestDan(unittest.TestCase):
    d = webdriver.Firefox(executable_path="e:\\geckodriver")
    d.get("http://localhost:8080/test/reg.jsp")
    def test_(self):
        driver = self.driver
        driver.get(self.base_url + "/test/mer.do?method=browseIndexMer")
        driver.find_element_by_name("btn").click()
        driver.find_element_by_name("memberName").clear()
        driver.find_element_by_name("memberName").send_keys("ii")
        driver.find_element_by_name("loginName").clear()
        driver.find_element_by_name("loginName").send_keys("ii")
        driver.find_element_by_name("loginPwd").clear()
        driver.find_element_by_name("loginPwd").send_keys("ii")
        driver.find_element_by_id("reLoginPwd").clear()
        driver.find_element_by_id("reLoginPwd").send_keys("ii")
        driver.find_element_by_name("phone").clear()
        driver.find_element_by_name("phone").send_keys("15284957435")
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(u"山东")
        driver.find_element_by_name("zip").clear()
        driver.find_element_by_name("zip").send_keys("110119")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("qwa@qq.com")
        driver.find_element_by_name("C_Input").click()

        driver.find_element_by_css_selector("span.whiteTitle").click()

        driver.find_element_by_name("loginName").clear()
        driver.find_element_by_name("loginName").send_keys("ii")
        driver.find_element_by_name("loginPwd").clear()
        driver.find_element_by_name("loginPwd").send_keys("ii")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_css_selector("span.blueText").click()

    """
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException,e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException,e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
"""
if __name__ == "__main__":
    unittest.main()
