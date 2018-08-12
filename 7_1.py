# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 12:23:38 2018

@author: NEVERGUVEIP
7-1 正则表达式

不用正则表达式判断电话号码
截取一段字符串的一部分如message[1:4],,是分号，分号，不是逗号

"""
def is_phone_number(message):
    if len(message)!=12:
        return False
    for i in range(3):
        if not message[i].isdecimal():#isdecimal()是判断给的字符是不是数字
            return False
    if message[3]!='-':
        return False
    for i in range(4,7):
        if not message[i].isdecimal():
            return False
    if message[7]!='-':
        return False
    for i in range(8,12):
        if not message[i].isdecimal():
            return False
    return True
    #print(message+'is a phone number')
    

#message='412-333-3232'
message='fefwfw321-245-3421 dsfergdgsdgsgsdrgsss'
print(message[0:5])#截取有一段字符串

for i in range(len(message)):
    text=message[i:i+12]
    if is_phone_number(text):
        print('phone number find ‘'+text+'’')
    
    
#print(is_phone_number(message))
