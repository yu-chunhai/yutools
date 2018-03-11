# coding=utf-8
# @作者:yuLearn
#@Time:2018/3/1-17:14
#@文件名称:yu-chunhai-键盘事件
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 删除键
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
# 空格键
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
# 制表键
driver.find_element_by_id("kw").send_keys(Keys.TAB)
# 回退键
driver.find_element_by_id("kw").send_keys(Keys.ESCAPE)
# 回车键
driver.find_element_by_id("kw").send_keys(Keys.ENTER)
# ctrl键，可以a,c,x,v进行组合
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')


driver.find_element_by_id("kw").send_keys("selenium")
time.sleep(3)
# 删除多输入的一个m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
time.sleep(3)
# 输入空格键+"教程"
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
driver.find_element_by_id("kw").send_keys(u"教程")
time.sleep(3)

# ctrl+a
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
time.sleep(3)

# ctrl+x
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
time.sleep(3)

# ctrl+v
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')
time.sleep(3)

# enter
driver.find_element_by_id("su").send_keys(Keys.ENTER)
time.sleep(3)

driver.close()
