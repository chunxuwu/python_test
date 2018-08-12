# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 23:33:03 2018

@author: NEVERGUVEIP
"""

#def strip(text):
#    import regex as re
#    mo=re.compile(r'^\S*|\S*$')
#    jud=mo.search(text)
#    if jud==None:
#        print('请输入字符')
#        return
#    print(jud.group())
#
#count=0   
#while count<5:
#    
#  text=input()
#  strip(text)
#  count+=1

def strip(text, chars=None):
    """去除首尾的字符
    
    :type text: string
    :type chars: string
    :rtype: string
    """
    import regex as re
    if chars is None:
        reg = re.compile('^ *| *$')
    else:
        reg = re.compile('^[' + chars + ']*|[' + chars + ']*$')
    return reg.sub('', text)

text=input()
print(strip(text))  




