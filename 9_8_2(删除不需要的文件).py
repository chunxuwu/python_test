# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 17:03:03 2018
删除不需要的文件夹，比如超过100m的文件（os.path.getsize()）

这里是显示字节数大于10的文件
@author: NEVERGUVEIP
"""

import os
#,shutil,send2trash
#print(os.walk('.\\test'))
for foldname,subfoldnames,filenames in os.walk('.\\test'):
#    print('we are now in'+foldname)
#    print(filenames)
    
    for filename in filenames:
        #if os.path.getsize(filename)<1024*100:
        #要获取系统的绝对路径
        if os.path.getsize(os.path.join(foldname,filename))>10:
            #send2trash(filename)
             print(filename)