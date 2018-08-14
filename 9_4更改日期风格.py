# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 21:49:51 2018

9.4 将美国风格日期的文件改名为欧洲风格

下面是程序要做的事： 
•  检查当前工作目录的所有文件名，寻找美国风格的日期。
•  如果找到，将该文件改名，交换月份和日期的位置，使之成为欧洲风格。 这意味着代码需要做下面的事情：
•  创建一个正则表达式，可以识别美国风格日期的文本模式。
•  调用 os.listdir()，找出工作目录中的所有文件。 
•  循环遍历每个文件名，利用该正则表达式检查它是否包含日期。 
•  如果它包含日期，用 shutil.move()对该文件改名。 对于这个项目，
打开一个新的文件编辑器窗口，将代码保存为 renameDates.py

@author: NEVERGUVEIP
"""
import re,os,shutil

#创建一个匹配美国风格日期的正则表达式

datePattern = re.compile(r'''
	^(.*?)			#匹配日期开始前的所有文本
	((0|1)?\d)-		#匹配月份
	((0|1|2|3)?\d)- #匹配日期
	((19|20)?\d)	#匹配20世纪和21世纪的年份
	(.*?)$
	''',re.VERBOSE)

print(os.listdir('.')) 
for amerFilename in  os.listdir('.'):
    mo = datePattern.search(amerFilename)
    if mo == None:
		# print('不匹配')
        continue
	 #符合规则将每一块信息保存到变量
	 # print(mo.group(1))
    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)
   
    euroFileName = beforePart + dayPart + '-'+ monthPart + '-' + yearPart + afterPart  
   # euroFileName = beforePart + 'spam_' + dayPart + '-'+ monthPart + '-' + yearPart + afterPart 
    
    absFilename = os.path.abspath('.')
    amerFilename = os.path.join(absFilename,amerFilename)
    euroFileName = os.path.join(absFilename,euroFileName)
    print('Renaming:\n %s \n To: \n%s' % (amerFilename,euroFileName))
    shutil.move(amerFilename,euroFileName)
