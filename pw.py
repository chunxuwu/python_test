#! python3
# pw.py - An insecure password locker program
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 11:29:41 2018
6.3  项目：口令保管箱 
@author: NEVERGUVEIP

要把该文件所在的目录添加至环境变量

bat文件中是python.exe,,,,不是py.exe
bat文件保存在windows系统目录下

win+r运行脚本是不需要带尖括号<>
直接输入 pw email就行了
"""

import pyperclip
import sys

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit() 
 
account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account) 