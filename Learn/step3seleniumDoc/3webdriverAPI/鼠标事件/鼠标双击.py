# coding=utf-8
# @作者:yuLearn
#@Time:2018/3/2-9:05
#@文件名称:yu-chunhai-鼠标双击
from selenium.webdriver.common.action_chains import ActionChains
# ActionChains.double_click()双击
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
right = driver.find_element_by_xpath('//*[@id="su"]')
ActionChains(driver).double_click(right).perform()
time.sleep(5)
driver.close()