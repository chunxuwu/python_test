#！python3 
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 09:50:15 2018

用一个关键字一段剪贴板文字

运行 py mcb.pyw save spam
当前剪贴板的内容用spam保存
通过运行 py mcb.pyw spam 
将文本加载到剪贴板
py mcb.pyw list 
将所有关键字的列表复制到剪贴板




@author: NEVERGUVEIP
"""

import shelve
import pyperclip,sys


mcbShelf=shelve.open('mcb')

#TODO:  保存剪贴板内容
if len (sys.argv)==3 and sys.argv[1].lower()=='save':
    mcbShelf[sys.argv[2]]=pyperclip.paste()
elif len(sys.argv)==2:
    if sys.argv[1].lower()=='list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    


#TODO：列出关键字，极其内容


mcbShelf.close()


