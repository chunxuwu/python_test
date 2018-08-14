# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 16:29:12 2018

第9章 组织文件

遍历目录树
os.walk()是遍历当前目录，

打印一个文件夹下所有子文件夹及文件

@author: NEVERGUVEIP
"""

import os

for folderName,subfolders,filenames in os.walk(r'C:\Users\NEVERGUVEIP\Documents\GitHub\python_test'):

    print('the current folder is '+folderName)
    print('-------------------------------------------------')
    for subfolder in subfolders:
        print('subfoler of'+folderName+':'+subfolder)
        
    print('------------------------------------------------')
    for filename in filenames:
        print('file inside'+folderName+':'+filename)
    
    print('')
    
    #1．当前文件夹名称的字符串。
    #2．当前文件夹中子文件夹的字符串的列表。
    #3．当前文件夹中文件的字符串的列表
    #
    #