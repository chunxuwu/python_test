# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 19:13:22 2018

@author: NEVERGUVEIP





"""
import pprint

message ='It is a beautiful day'
count={}

for character in message:
    count.setdefault(character,0)
    count[character]=count[character]+1#返回的是键的值
    
pprint.pprint(count)