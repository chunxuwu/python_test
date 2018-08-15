# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 08:44:12 2018

10.3 在交通灯模拟中使用断言




@author: NEVERGUVEIP
"""


market_2nd = {'ns':'green','ew': 'red'}

def switchLights(stoplight):
    for key in stoplight.keys():
        
        if stoplight[key] == 'green':#会循环出现黄、绿灯同时亮的情况
            stoplight[key] = 'yellow'
        elif stoplight[key] =='yellow':
            stoplight[key] == 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    #确保 至少有一个灯是红灯
    assert 'red' in stoplight.values(), 'Neither light is red!' + str(stoplight)

switchLights(market_2nd)
        
        