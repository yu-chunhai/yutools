# coding=utf-8
# @作者:yuchunhai
#@Time:2017/12/19-11:05
#@文件名称:py3Test-test1
import flask
app = flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()