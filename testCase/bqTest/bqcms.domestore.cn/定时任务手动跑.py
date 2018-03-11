# coding=utf-8
# @作者:yuchunhai
#@Time:2017/12/25-19:51
#@文件名称:py3Test-定时任务手动跑
import requests
import json
url = "http://bqcms.domestore.cn/test/load"
payload = {

}
r = requests.get(url, params=payload)
print(r.json())