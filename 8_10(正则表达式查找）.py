# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 15:45:18 2018

8.9.3  正则表达式查找  

第一步：以正则的方式获取当前目录所有txt文件


@author: NEVERGUVEIP
"""


import re
import os

cwd=os.getcwd()

txtDirList=[]

regex1=re.compile(r'\.txt$')#在字符结束的地方匹配，不匹配任何字符

for x in os.listdir(cwd):

    if regex1.search(x)!=None:

        txtDirList.append(x)

print(txtDirList)

#print(sys.argv[1])

regex2=re.compile(r'[a-z]{3}')

txtLineList=[]

for x in txtDirList:

    with open(x) as txtFile:

        txtLineList=txtFile.readlines()#读取字符串列表，每个字符串以换行符\n结束。

        for y in txtLineList:

            if regex2.search(y)!=None:

                print(y)
