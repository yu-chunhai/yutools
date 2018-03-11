# coding=utf-8
# @作者:yuLearn
#@Time:2018/3/1-17:52
#@文件名称:yu-chunhai-定位一组元素
from selenium import webdriver
import os
import time

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('checkbox.html')
driver.get(file_path)
# 失败
# inputs = driver.find_element_by_tag_name('input')
# for input in inputs:
#     if input.get_attribute('type') == 'checkbox':
#         input.click()
# 错误
# checkboxes = driver.find_element_by_css_selector('input[type=checkbox]')
checkboxes = driver.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxes:
    checkbox.click()
# 打印个数
print(len(driver.find_elements_by_css_selector('input[type=checkbox]')))
# 把最后一个checkbox的勾去掉
driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()
time.sleep(5)
driver.quit()