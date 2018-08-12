# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 15:35:06 2018

@author: NEVERGUVEIP
"""

import regex as re 
 
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                 # area code
    (\s|-|\.)?                         # separator
    (\d{3})                            # first 3 digits     
    (\s|-|\.)                          # separator
    (\d{4})                            # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?     # extension
    )''', re.VERBOSE) 

print(phoneRegex.search('222-334-3321').group())
