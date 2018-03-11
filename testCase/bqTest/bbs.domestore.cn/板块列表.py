# coding=utf-8
# @作者:yuchunhai
#@Time:2017/12/25-16:08
#@文件名称:py3Test-板块列表
import requests
import json

url = "http://bbs.domegame.cn/api/mobile/index.php"
payload = {"version":"1","module":"forumindex"}
r = requests.get(url, params=payload)
print(r.json()['Variables']['catlist'])