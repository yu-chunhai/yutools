# coding=utf-8
# @作者:yuLearn
#@Time:2018/3/2-9:05
#@文件名称:yu-chunhai-鼠标右击
from selenium.webdriver.common.action_chains import ActionChains
# ActionChains.context_click()右击
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
right = driver.find_element_by_xpath('//*[@id="su"]')
ActionChains(driver).context_click(right).perform()
time.sleep(5)
driver.close()