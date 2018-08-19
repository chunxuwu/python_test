# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 15:25:30 2018

12.10.3冻结窗格
设置                            冻结的行和列
sheet.freeze_panes='A2'            行1
‘B1’                  列A
‘C1‘                  列A和列B
’C2‘                  行1、列A和B
“A1”或’NONE’          解冻


@author: NEVERGUVEIP
"""
import openpyxl
path = r'.\automate_online-materials\produceSales.xlsx'
wb = openpyxl.load_workbook(path,data_only=True)
sheet = wb.get_active_sheet()

sheet.freeze_panes = 'A2'

wb.save('freezeExample.xlsx')
