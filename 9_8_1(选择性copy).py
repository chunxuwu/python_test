# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 15:58:19 2018

编了一个目录，查找特定扩展名的文件并复制其到新的文件夹
1、遍历目录需要os.walk(),复制需要shutil模块
2、先创建一个文件夹用于要保存的文件
3、遍历文件，找到符合条件的文件并防止复制要备份的文件
4、复制符合条件的文件到目标文件夹



@author: NEVERGUVEIP
"""
#! python3
import os ,shutil

try:#抛出多次运行时建立文件夹的错误
    mydir = 'new dir'
    os.makedirs(mydir)
except FileExistsError:
    pass

for foldername,subfolds,filenames in os.walk('.'):#遍历当前文件夹的树目录
    
    for filename in filenames:#找出以txt或pdf为后缀名的文件
        if filename.endswith('.txt') or filename.endswith('.pdf'):
            #排除自己复制自己
            if filename not in os.listdir(mydir):#把符合条件的文件复制到新建的文件夹
                shutil.copy(os.path.join(foldername,filename),mydir)