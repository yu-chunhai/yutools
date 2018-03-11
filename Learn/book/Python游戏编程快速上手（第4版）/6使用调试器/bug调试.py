# coding=utf-8
# @作者:yuLearn
#@Time:2018/2/28-8:50
#@文件名称:yu-chunhai-bug调试
import random
number1 = random.randint(1, 10)
number2 = random.randint(1, 10)
print('What is ' + str(number1) + ' + ' + str(number2) + '?')
answer = input()
if answer == number1 + number2:
    print('Correct!')
else:
    print('Nope! The answer is ' + str(number1 + number2))