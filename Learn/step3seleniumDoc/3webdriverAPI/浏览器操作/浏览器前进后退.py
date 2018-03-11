# coding=utf-8
# @作者:yuLearn
#@Time:2018/3/2-8:56
#@文件名称:yu-chunhai-浏览器前进后退
from selenium import webdriver
import time
driver = webdriver.Chrome()

one_url = 'https://www.baidu.com'
driver.get(one_url)
time.sleep(2)

two_url = 'https://news.baidu.com'
driver.get(two_url)
time.sleep(2)

print('one_url')
driver.back()
time.sleep(2)

print('two_url')
driver.forward()
time.sleep(2)

driver.close()