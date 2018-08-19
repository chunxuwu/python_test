# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 13:59:19 2018

11.4 HTML超文本标记语言

HTML文件是一个纯文本文件，带有.html文件扩展名。这种文件中的文本被标签环绕，标签是尖括号
包围的单词。标签告诉浏览器以怎样的格式显示该页面。一个开始标签和一个结束标签可以包围某段文本
形成一个‘元素’，文本是开始标签和结束标签之间的内容。
html有许多不同的标签，有一些具有额外的特性，在尖括号内以‘属性’的方式展现，例如,<a>标签包含
一个链接。

不要正则表达式来解析HTML

利用浏览器的开发者工具，来查看网页的HTML，找到html元素

利用BeautifulSoup模块解析HTML


"""
import requests,bs4

res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text,"lxml")
type(noStarchSoup)


#创建一个bs4对象
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile,"lxml")
type(exampleSoup)