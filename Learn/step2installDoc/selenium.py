# coding=utf-8
# @作者:Administrator
#@Time:2018/3/11-14:50
#@文件名称:yu-chunhai-selenium
import os
# 方法一离线安装
# import profileDoc.importRoot
# selenium390Root = profileDoc.importRoot.selenium390
# os.chdir(selenium390Root)
# os.system('python setup.py install')

# 方法二在线安装
import Learn.profileDoc.pythonRoot
tarRoot =  Learn.profileDoc.pythonRoot.python364 +  r'\Scripts'
tar = 'selenium'
os.chdir(tarRoot)
os.system(r'pip install ' + tar)