#! python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 21:27:42 2018
6.4  项目：在 Wiki 标记中添加无序列表 

@author: NEVERGUVEIP

手动复制的字符串要带上单括号的，要不让不对

脚本文件不要有其他字符


@python.exe ........\pw.py %* 
是python
@pause
"""

# bulletPointAdder.py - Adds Wikipedia bullet points to the start 
# of each line of text on the clipboard. 
 
import pyperclip


text = pyperclip.paste() 
#text='Lists of animals\nLists of aquarium life\nLists of biologists by author abbreviation\nLists of cultivars '
# Separate lines and add stars. 
lines = text.split('\n')
for i in range(len(lines)): # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list 
text = '\n'.join(lines) 
pyperclip.copy(text) 

#'Lists of animals\nLists of aquarium life\nLists of biologists by author abbreviation\nLists of cultivars '

#* Lists of animals
#* Lists of aquarium life
#* Lists of biologists by author abbreviation
#* Lists of cultivars 