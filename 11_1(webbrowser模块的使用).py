# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 12:01:15 2018

打开谷歌地图
@author: NEVERGUVEIP
"""
#！ python3
import webbrowser,sys,pyperclip
#打开百度首页，在默认浏览器中显示

if len(sys.argv) > 1:
    address = ''.join(sys.argv[1:])#argv[0]返回的是文件名，
    
#TODO get address from clipboard.
else:
    #get adress from clipboard
    adress = pyperclip.paste()
    
    

webbrowser.open('https://www.google.com/maps/place/'+adress)
