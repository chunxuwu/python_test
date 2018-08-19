# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 09:28:11 2018

@author: NEVERGUVEIP
"""
import logging,bs4

logging.basicConfig(level=logging.DEBUG, 
                    format = '%(asctime)s - %(levelname)s - %(message)s')

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(),'lxml')
elems = exampleSoup.select('#author')

elems[0].getText()

print(str(elems[0]))

print(elems[0].attrs)

pElems = exampleSoup.select('p')

pElems[0].getText()

pElems[1].getText()
print(pElems[2].getText())

#通过元素的属性获取数据  10.5.3
exampleFile = open('example.html')##为啥还要open一遍，不open还报错
soup = bs4.BeautifulSoup(exampleFile,'lxml')
spanElem = soup.select('span')[0]
str(spanElem)
spanElem.get('id')

if spanElem.get('some_nonexitent_addr') == None:
    print(spanElem.attrs)















