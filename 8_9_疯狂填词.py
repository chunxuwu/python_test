# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 14:25:47 2018

方法步骤：

		1.导入文本

		2.循环查找并替换

		3.打印结果，保存为另一个新的文件
@author: NEVERGUVEIP
"""
#! python3
#疯狂填词



#疯狂填词-替换文本文件中的单词

'''

	方法步骤：

		1.导入文本

		2.循环查找并替换

		3.打印结果，保存为另一个新的文件

'''

#打开文件,并读取内容

myFile = open('words.txt','r')

myNewFile = open('newwords.txt','w')

text = myFile.read()

 

wordsReplace = ['ADJECTIVE','NOUN','ADVERB','VERB']

wordsLength = len(wordsReplace)

#替换单词

for i in range(wordsLength):

	print('Enter an '+ wordsReplace[i].lower()+' :')
	word = input()
	text = text.replace(wordsReplace[i],word)

#将新的文本装入一个新的文件中

myNewFile.write(text)
#要先关闭在打开
myFile.close()
myNewFile.close()

 

