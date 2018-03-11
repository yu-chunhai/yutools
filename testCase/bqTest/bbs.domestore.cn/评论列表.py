# coding=utf-8
# @作者:yuchunhai
#@Time:2017/12/25-16:28
#@文件名称:py3Test-评论列表
import requests
import json

url = "http://bbs.domegame.cn/api/mobile/index.php"
payload = {"version":"1","module":"viewthread","tid":"14","page":"1","ppp":"30"}
r = requests.post(url, params=payload)
print(r.text)