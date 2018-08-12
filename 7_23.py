# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 22:26:57 2018

正则表达式怎么统计长度呢：

@author: NEVERGUVEIP
"""

import regex as re

def name(text):
    if len(text)<8:
        print('请输入长度大于8的字符串')
        return
    else:
        reg1=re.compile('[A-Z]+')
        if reg1.search(text)==None:
            print('请输入带有大写字母的字符串')
            return
        
        reg2=re.compile('[a-z]+')
        if reg2.search(text)==None:
            print('请输入带有小写字母的字符串')
            return
        reg3=re.compile('\d+')
        if reg3.search(text)==None:
            print('请输入带有数字的字符串')
            return
        print('您的字符串符合要求')
        return

count=0
while count<5:
   text=input()
   name(text)
   count += 1        
   
        
        

#dog=re.compile(r'([A-Z]+[a-z]+\d+)|([A-Z]+\d+[a-z]+|[a-z]+[A-Z]+\d+|[a-z]+\d+[A-Z]+|\d+[A-Z]+[a-z+]|\d+[a-z]+[A-Z]+)')
#不能解决乱排序的问题
