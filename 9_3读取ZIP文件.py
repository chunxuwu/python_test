# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 20:54:41 2018

9.3 用zipfile模块压缩文件

1、读取zip文件
2、从zip文件中解压
3、创建添加到ZIP文件

@author: NEVERGUVEIP
"""

import os,zipfile

os.chdir(r'C:\Users\NEVERGUVEIP\Documents\GitHub\python_test')

exampleZip=zipfile.ZipFile('example.zip')

print(exampleZip.namelist())

mcbInfo=exampleZip.getinfo('mcb.pyw')

print('源文件大小'+str(mcbInfo.file_size)+', 压缩后文件大小'+str(mcbInfo.compress_size))

print('压缩率为%sx'%(round(mcbInfo.file_size/mcbInfo.compress_size,2)))

exampleZip.close()


##解压zip文件
os.chdir(r'C:\Users\NEVERGUVEIP\Documents\GitHub\python_test')
exampleZip1=zipfile.ZipFile('example.zip')
exampleZip1.extractall()#解压全部文件到当前文件夹
#exampleZip1.extracall(r'C:\delicious')#解压文件到指定目录，如果问件夹不存在，就会创建指定文件夹
exampleZip1.close()


##创建和添加到ZIP文件

newZip=zipfile.ZipFile('new.zip','w')#写模式将擦除压缩包中原有内容
newZip.write('heheheh.txt',compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
