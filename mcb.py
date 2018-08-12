#！python3 
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 09:50:15 2018

8-6多重剪贴板

用一个关键字一段剪贴板文字

#这是在python环境下运行的
#运行 py mcb.pyw save spam
#当前剪贴板的内容用spam保存
#通过运行 py mcb.pyw spam 
#将文本加载到剪贴板
#py mcb.pyw list 
#将所有关键字的列表复制到剪贴板
'''
'''
#要想用windows脚本运行
#直接 mcb save spamS
#mcb spam
#mcb list
#\s
@python.exe  %*
@pause
#
#我的批文件内容是这样的，保存在windows下
#网上搜了一下，.py与.pyw差不多,没什么区别

#@author: NEVERGUVEIP


sys.argv[0]是文件名
sys.argv[1]是传入的第一个参数
。。。
"""
#不能、\U
import shelve
import pyperclip,sys


mcbShelf=shelve.open('mcb')

#TODO:  保存剪贴板内容
if len (sys.argv)==3 :
    
    if sys.argv[1].lower()=='save':
        mcbShelf[sys.argv[2]]=pyperclip.paste()
        
    elif sys.argv[1].lower()=='delete':
        del mcbShelf[sys.argv[2]]
        
elif len(sys.argv)==2:
    
    if sys.argv[1].lower()=='list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        
    elif sys.argv[1].lower()=='delete':
        mcbShelf.clear()
        
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    


#TODO：列出关键字，极其内容


mcbShelf.close()


