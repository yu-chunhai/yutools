# coding=utf-8
# @作者:yuLearn
#@Time:2018/2/7-19:08
#@文件名称:yu-chunhai-浏览器打开百度
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(5)
driver.close()