# coding=utf-8
# @作者:yuLearn
#@Time:2018/2/23-13:43
#@文件名称:yu-chunhai-seleniumForYu-chunhai
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://github.com/login")
driver.find_element_by_xpath('//*[@id="login_field"]').send_keys("18905255025@163.com")
driver.find_element_by_xpath('//*[@id="password"]').send_keys("yuchunhai1989")
driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[3]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="your_repos"]/div/div[2]/ul/li/a/span/span').click()
time.sleep(5)
driver.close()