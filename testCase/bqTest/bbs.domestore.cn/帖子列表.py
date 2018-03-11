# coding=utf-8
# @作者:yuchunhai
#@Time:2017/12/25-16:26
#@文件名称:py3Test-帖子列表
import requests
import json

url = "http://bbs.domegame.cn/api/mobile/index.php"
payload = {"version":"1","module":"forumdisplay","fid":"38"}
r = requests.post(url, params=payload)
print(r.json())