# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 14:30:09 2018

11.8 用slenium模块控制浏览器
启动火狐浏览器
WebDriverException: 'geckodriver' executable needs to be in PATH. 
下载geckodriver.exe  并且把它的路径设置为系统路径

根据模拟鼠标点击当前网页的链接
@author: NEVERGUVEIP
"""

#点击页面
from selenium import webdriver
browser = webdriver.Firefox()
#browser.get('http://inventwithpython.com')
#
#linkElem = browser.find_element_by_link_text('YouTube')#可以的
#
#linkElem.click()
##try:
##    elem = browser.find_element_by_class_name('bookcover')
##    print('Found <%> element with that class name!'%(elem.tag_name))
##except:
##    print('Was not able to find an element with that name')

#这个没有成功
browser.get('http://gmail.com')
emailElem = browser.find_element_by_id('Email')
emailElem.send_keys('neverguveip@gmail.com')
passwordElem = browser.find_element_by_id('Passwd')
passwordElem.send_keys('wcx1234567890')
passwordElem.submit()