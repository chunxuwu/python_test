# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 21:56:37 2018

@author: NEVERGUVEIP
"""
import regex as re

name=re.compile(r'^[A-Z][a-z]*\sNakamoto')

print(name.search('Alice Nakamoto').group())

print((name.search('alice Nakamoto'))==None)


