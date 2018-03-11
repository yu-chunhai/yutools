# coding=utf-8
# @作者:yuchunhai
#@Time:2017/12/25-15:26
#@文件名称:py3Test-用户信息获取
import requests
import json

url = "http://bbs.domegame.cn/api/post.php"
payload = {"mod":"uc_user_info","username":"bq_000230018"}
r = requests.post(url, params=payload)
print(r.text)