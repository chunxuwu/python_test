# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 22:33:26 2018
6-7 项目
表格打印

@author: NEVERGUVEIP
"""

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

#num_list=[len(one) for one in tableData]
#这是获得列表的shape
def printTable(tableData):
    
	maxlist = []
	for i in tableData:#每一行每一行的取出来
      
		linemax = max([len(lenght) for lenght in i])#
		maxlist.append(linemax)
	for x in range(len(tableData[0])):
		for j in range(len(tableData)):
			print(tableData[j][x].rjust(maxlist[j]),end=' ')
		print()
	
printTable(tableData)

print(len(tableData))#3列表是行数
print(len(tableData[0]))#4,是第一行列表的元素数目
print(tableData)