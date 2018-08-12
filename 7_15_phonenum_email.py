#! python3 
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 13:33:18 2018
7.15  项目：电话号码和 E-mail 地址提取程序 
https://woodpecker.org.cn/diveintopython/regular_expressions/phone_numbers.html
这是详细介绍

info@nostarch.com
media@nostarch.com

eqrgwerge415-863-9900fgwrgw 
415-863-9950 

re.VERBOSE 标志有这么几个作用。在正则表达式中不在字符类中的空白符被忽略。
这就意味着象 dog | cat 这样的表达式和可读性差的 dog|cat 相同，但 [a b] 
将匹配字符 "a"、"b" 或 空格。另外，你也可以把注释放到 RE 中；注释是从 "#" 
到下一行。当使用三引号字符串时，可以使 REs 格式更加干净：

group返回字符串
'415-555-4242'
groups返回字符串列表
('415', '555-4242')
@author: NEVERGUVEIP


"""

# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard. 
 
import pyperclip
import regex as re 
 
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                 # area code要有就有三个数字或带有括号的3个数字，也可以没有
    (\s|-|\.)?                         # separator
    (\d{3})                            # first 3 digits     
    (\s|-|\.)                          # separator 空格、-或者点(.)
    (\d{4})                            # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?     # extension 800-555-1212 ext. 1234 后面的是分机号
                                       # 这个竟然占三组
                                       #
    )''', re.VERBOSE) 
#邮件正则
emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+   # username
        @                   # @ symbol
        [a-zA-Z0-9.-]+      # domain name     
        (\.[a-zA-Z]{2,4})   # dot-something 
        )''', re.VERBOSE)
 
# TODO: Find matches in clipboard text.
text = str(pyperclip.paste())

matches = [] 
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]]) 
    if groups[8] != '':         #总共不是定义6组吗，，哪来的8呢，，谁能解答呀
                                #group=('415-555-4242', '415', '-', '555', '-', '4242', '', '', '')
                                #group[1]='425'
        phoneNum += ' x' + groups[8]
        
    matches.append(phoneNum)
for groups in emailRegex.findall(text):     
    matches.append(groups[0])
 
# TODO: Copy results to the clipboard.
if len(matches)>0:
	pyperclip.copy('\n'.join(matches))
	print('Copy to clipboar')
	print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.') 

    