#！ python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 10:16:17 2018

11.6‘I'm Feeling Lucky’ Google 查找

根据关键词打开Google中前几个链接

1、从命令行参数获取查询的关键字
2、取得查询结果的界面
3、为每个结果打开选显卡

步骤：
a、从sys.argv中读取命令行参数
b、用requests模块取得查询结果页面
c、找到每一个查询结果的链接
d、调用webbrowser。open（）函数打开web浏览器

@author: NEVERGUVEIP
"""

import requests,sys,webbrowser,bs4
print('Googling...')
res = requests.get('http://google.com/search?q=' +' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,'lxml')

#定位链接
linkElems = soup.select('.r a')

numOpen = min(5,len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com'+linkElems[i].get('href'))
    #在新的选项卡中查询前5个结果或列表的长度

