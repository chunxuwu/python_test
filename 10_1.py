# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 09:30:12 2018
第十章调试
1、抛异常
利用raise 优雅的处理异常
try:
    bocPtint(sym,w,h)
except Exception as err:
    print('an exception happened: '+str(err))
    
@author: NEVERGUVEIP
"""

def boxPrint(symbol,width,height):
    if len(symbol)!=1:
        raise Exception('Symbol must be a single chatacter string.')
    if width <=2:
        raise Exception('width must be greater than 2')
    if height <= 2:
        raise Exception('height must be greater than 2')
        
    print(symbol * height)
    for i in range(width - 2):
        print(symbol + (' '*(height-2)) + symbol)
    print(symbol * height)
    
for sym ,w ,h in (('*',4,4),('0',5,20),('x',1,3),('zz',3,3)):
    try:
        boxPrint(sym,w,h)
    except Exception as err:
        print('an exception happened:'+str(err))
        
    