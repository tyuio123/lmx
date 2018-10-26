from selenium import webdriver


d = webdriver.Firefox(executable_path = "e:\\geckodriver")
d.get("file:///F://智郎瑞博/工具大全/第三阶段/工具/coshttp/demo.html")
#d.get("https://baidu.com")
#s = d.find_element_by_id("kw")
s = d.find_element_by_id("user")
s.clear()
s.send_keys("我女儿是你女儿的妈妈，我是你的谁")

p = d.find_element_by_class_name("baidu").click()
d.back()
#dianji = d.find_element_by_id("su")
#dianji.click()
x = d.find_element_by_name("select")
x.find_element_by_xpath(".//option[@value='audi']").click()
d.maximize_window()

w = d.find_element_by_class_name("Opel").click()

e = d.find_element_by_name("checkbox1").click()
r = d.find_element_by_name("checkbox2").click()
t = d.find_element_by_name("checkbox3").click()

y = d.find_element_by_xpath(".//input[@value='Submit']")

d.find_element_by_class_name("Alert").click()
u = d.switch_to_alert()
print(u.text)
u.accept()

i = d.find_element_by_id("load").send_keys(r"G:\图片\fc8fc02bd14fc2db.jpg")

o = d.find_element_by_class_name("open").click()
d.switch_to().window('handle')























