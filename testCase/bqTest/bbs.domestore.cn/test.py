# coding=utf-8
# @作者:yuchunhai
#@Time:2017/12/25-16:33
#@文件名称:py3Test-test
import requests
import json

url = "http://bbs.domegame.cn/api/post.php"
payload = {"mod":"get_thread_post","fid":"36","tid":"3"}
r = requests.post(url, params=payload)
print(r.text)