# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 22:02:34 2018

@author: NEVERGUVEIP
"""

import regex as re

sen=re.compile(r'Alice|Bob|Carol\s(eat|pet|throws)\s(apple|cats|baseballs)',re.IGNORECASE)

print(sen.search( 'Carol throws baseballs.').group())