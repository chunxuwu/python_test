# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 13:32:25 2018

用request.get()下载一个网页

1、调用request.get()下载该文件
2、用‘wb’调用open(),以写二进制的方式打开一个新文件
3、利用Reapose对象的iter_cintent()方法做循环
4、在每次迭代中调用writer（），将内容写入该文件
5、调用close（）关闭该文件
@author: NEVERGUVEIP
"""

import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
type(res)

res.raise_for_status()
res.status_code == requests.codes.ok

len(res.text)


playFile = open('romeoAndJuliet.txt','wb')

for chunk in res.iter_content(100000):#确保即使下载巨大文件时也不会消耗太多内存
    playFile.write(chunk)

playFile.close()
#print(res.text[:250])