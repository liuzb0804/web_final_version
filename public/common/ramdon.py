# coding=utf-8
import random
import string
import sys

def ramdondata(data):
    #存储大小写字母和数字，特殊字符列表
    STR = [chr(i) for i in range(65,91)]   #65-91对应字符A-Z
    str = [chr(i) for i in range(97,123)]   #a-z
    number = [chr(i) for i in range(48,58)]  #0-9

    #特殊字符串列表获取有点不同
    initspecial = string.punctuation      #这个函数获取到全部特殊字符，结果为字符串形式
    special = []                          #定义一个空列表

    #制作特殊符号列表
    for i in initspecial:
        special.append(i)

    total = STR + str + number + special
    passwordli = random.sample(total, data)
    passwordst = ''.join(passwordli)
    return passwordst



# f = ramdondata(61)
#
# print(f)

