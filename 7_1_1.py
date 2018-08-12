# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 13:15:04 2018
7-2 正则表达式练习

正则模块安装 pip install regex  
不是re

@author: NEVERGUVEIP
"""
import regex as re

num=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#r''表示将该字符串表示为原始字符串，不包含转义字符

#search()方法将返回一个Match 对象

find_num=num.search('dnfoaef212-333-4213')
#group()方法，它返回被查找字 符串中实际匹配的文本
print(find_num.group())


