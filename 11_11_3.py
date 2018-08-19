# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 09:51:17 2018

@author: NEVERGUVEIP
"""

#！ python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')

htmlElem = browser.find_element_by_tag_name('html')


for i in range(1000):
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT)

print('done!')