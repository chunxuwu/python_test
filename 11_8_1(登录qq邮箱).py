# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 09:17:01 2018

#这模式是行不通了，

@author: NEVERGUVEIP
"""

# -*- coding:UTF-8 -*-
 
from selenium import webdriver

import time
 
# 模拟登陆qq邮箱
#driver = webdriver.Firefox(executable_path = 'D:\getckodriver\geckodriver')
driver = webdriver.Firefox()
driver.get("https://mail.qq.com/")
time.sleep(5)
# 切换iframe
driver.switch_to.frame("login_frame")
# 用户名 密码
elem_user = driver.find_element_by_name("u")
elem_user.send_keys("1293296315")
elem_pwd = driver.find_element_by_name("p")
elem_pwd.send_keys("wcx..123.....")
elem_but = driver.find_element_by_id("login_button")
# elem_pwd.send_keys(Keys.RETURN)
elem_but.click()
time.sleep(5)
# driver.quit()
