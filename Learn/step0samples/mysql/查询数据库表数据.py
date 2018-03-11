# coding=utf-8
# @作者:yuLearn
#@Time:2018/2/7-18:54
#@文件名称:yu-chunhai-查询数据库表数据
import pymysql
db = pymysql.connect("localhost","localhost","111111","mysql")
cursor = db.cursor()
sql = "SELECT * FROM mysql.user;"
cursor.execute(sql)
results = cursor.fetchall()
print(results)