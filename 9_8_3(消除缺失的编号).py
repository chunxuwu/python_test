# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 19:44:00 2018

9.8.3  消除缺失的编号 

@author: NEVERGUVEIP
"""
import os ,re, shutil

#dir=os.getcwd()
#print(dir)

absWorkingDir=os.path.abspath('.\\test')
print(absWorkingDir)

filenames=[x for x in os.listdir('.\\test') if '.' in x and x.startswith('t')]
#if '.' in x  可以稍微保证一下文件名中有.号，有后缀之类的,列表生成器
print(os.listdir('.\\test'))
print(filenames)

numRegex = re.compile(r'^test\d.txt$')

o_num_list=[]
for filename in filenames:
    
    name_re = numRegex.search(filename)
    
    o_num_list.append(name_re.group(0))
    
print(o_num_list)

n_num_list=[]
for i in range(1,len(o_num_list)+1):
    #t_i = '%03d' % i#用0填充2位数001,002
    #t_i = i
    n_num_list.append('test'+str(i)+'.txt')
print(n_num_list)

#for i in n_num_list:
#    if i not in o_num_list:
#        print(i)
        
#对文件改名以消除缺失的编号
for i,v in zip(o_num_list,n_num_list):
    #shutil.move(dir+'\\%s'%i,dir+'\\%s'%v)
    shutil.move(os.path.join(absWorkingDir,i),os.path.join(absWorkingDir,v))

print('rename project is done！')
        
        
        