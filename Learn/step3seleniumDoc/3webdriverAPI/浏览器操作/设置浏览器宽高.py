# coding=utf-8
# @作者:yuLearn
#@Time:2018/3/2-8:55
#@文件名称:yu-chunhai-设置浏览器宽高
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
print("设置浏览器宽高")
driver.set_window_size(480,800)
time.sleep(5)
driver.close()
