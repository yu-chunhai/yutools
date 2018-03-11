# coding=utf-8
# @作者:yuLearn
#@Time:2018/3/1-17:36
#@文件名称:yu-chunhai-设置等待时间
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# WebDriverWait()使用
# WebDriverWait(driver,timeout,poll_frequency=0.5,ignored_exceptions=None)

element = WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_id("kw"))
element.send_keys("selenium")
# 智能等待
driver.implicitly_wait(30)
driver.find_element_by_id("su").click()