# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 10:26:55 2018

@author: NEVERGUVEIP

第六章学习笔记
"""

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    #中间打印“PICNIC ITEMS”,俩边平均打印— 
    for k, v in itemsDict.items():
        #靠左打印，不够的用.补上，，同理v靠右打印
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))


picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000} 
printPicnic(picnicItems, 12, 6) 
printPicnic(picnicItems, 20, 6)

#删除字符串俩边的字符“Spam”，，和字母的排列顺序没有关系


spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam=spam.strip('ampS')
print(spam)

#用 pyperclip 模块拷贝粘贴字符串 
#如果在程序外复制了一些文字后在调用paste（），就会返回刚刚复制的文字
import pyperclip
pyperclip.copy('hello world')
print(pyperclip.paste())


#
print('\n')

