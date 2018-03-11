# coding=utf-8
# @作者:yuLearn
#@Time:2018/2/7-18:51
#@文件名称:yu-chunhai-内部链接redis
import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.69.232',22,username='root',password='bqceshi',timeout=4)
stdin,stdout,stderr = client.exec_command("cd /code_dir/gnsrc/store-admin/src;pwd;php artisan redis:reload --part=all",)
print(stdout.readlines())
client.close()