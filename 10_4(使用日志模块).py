# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 09:29:00 2018

10.4 日志
启用 logging 模块
logging.basicConfig(level=logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')

不要使用print调试，否则一个一个删很麻烦

日志的好处在于，可以随心所欲在程序中添加。。。

只要加入 logging.disable(logging.CRITICAL)调用，就可以禁日志

日志的级别有 DEBUG\INFO\WARING\ERROR\CRITICAL

将日志记录到文件
import logging
logging.basicConfig(filename='myProgramlog.txt',level=logging.DEBUG, format=
'%(asctime)s -%(levelname)s -%(message)s')


@author: NEVERGUVEIP
"""

import logging

logging.basicConfig(level=logging.DEBUG, 
                    format = '%(asctime)s - %(levelname)s - %(message)s')
logging.debug('start of program')

def factorial(n):
    logging.debug('start of factorial(%s%%)' %(n))
    total = 1
    for i in range(n+1):
        total*=1
        logging.debug('i is '+str(i)+ ', total is '+str(total))
    logging.debug('End of factorial(%s%%)'%(n))
    return total

print(factorial(5))
logging.debug('end of program')