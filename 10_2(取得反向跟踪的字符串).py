# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 10:08:05 2018

10.2 取得反向跟踪的字符串
反向跟踪
traceback.format_exc(),既可以反向跟踪错误信息也可以优雅的处理异常


@author: NEVERGUVEIP
"""

import traceback

def spam():
    bacon()
def bacon():
    raise Exception('this is the error message.')
    

try:
    spam()
    raise Exception('this is the error massage.')

except:
    errorFile = open('errorInfo.txt','w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    
    print('the traceback info was written to errorInfo.txt')
    