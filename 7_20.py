# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 21:10:37 2018

@author: NEVERGUVEIP
"""

import regex as re

num=re.compile(r'^\d{1,3}(,\d{3})*$')
#num=re.compile(r'\d{1:3}')#是逗号，不是分号


print(num.search('2,233,234,234').group())#2,233,234,234
print(num.findall('2,234,134,234'))#[',234']


