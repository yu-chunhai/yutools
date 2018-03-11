# coding=utf-8
# @作者:yuLearn
#@Time:2018/2/7-19:08
#@文件名称:yu-chunhai-百度搜索python关键字
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_xpath('//*[@id="kw"]').send_keys("python")
driver.find_element_by_xpath('//*[@id="su"]').click()
time.sleep(5)
driver.close()