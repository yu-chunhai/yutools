# coding=utf-8
# @作者:yuLearn
#@Time:2018/3/2-8:42
#@文件名称:yu-chunhai-浏览器最大化
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
print("浏览器最大化")
driver.maximize_window()
time.sleep(5)
driver.close()
