# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 14:05:19 2018
第12章处理excle电子表格

@author: NEVERGUVEIP
"""
对于以下问题，设想你有一个workbook对象保存在变量wb中，一个worksheet对象保存在sheet中，一个Cell对象保存在cell中，
一个Comment对象保存在comm中，一个Image对象保存在img中。
1、openpyxl.load_workbook()函数返回什么？
    返回一个Workbook数据类型的值
2、get_sheet_names()工作簿方法的返回什么?
    返回工作簿中的列表,Worksheet对象
3、如何取得名为‘sheet1’的工作表的Worksheet对象？
    wb=openpyxl.load_workbook('example.xlsx')
    wb.get_sheet_by_name('sheet1')
4、如何取得工作簿的活动工作表的Worksheet对象？
     wb.get_active_sheet()
5、如何取得单元格C5中的值
    sheet['C5'].value
6、如何将单元格C5的值设置为‘Hello’？
    sheet['C5'].value = 'Hello'
7、如何取得表示单元格的行和列的整数？
    cell.row和cell.column
8、工作表方法get_hight_column()和get_highest_row()返回什么？这些值的类型是什么？
    现在为max_column和max_row,返回值类型为int
9、如果要取得列‘M’的整数下标，需要调用什么函数？
    column_index_from_string('M')
10、如果要取得列14的字符串的名称，需要调用什么函数？
    get_column_letter(14)
11、如何取得从A1到F1的所有Cell对象元组？
    tuple(sheet['A1':'C3'])
12、如何在一个表格中设置公式？
    和设置其他文本一样,将单元格的value属性设置为公式文本的字符串。公式以=号开始
13、如何将工作簿保存到名为exampl.xlsx?
    wb.save('example.xlsx')
14、如何需要取得单元格中公式的结果，而不是公式本身，必须先做什么？
    在workbook的data_only参数设置为True
15、如何将第5行的高度设置为100？
    sheet.column_dimensions[5].height =100
16、如何设置列C的宽度？
    sheet.row_dimensions['C'].width = 20
17、列出一些openpyxl2.1.4不会从电子表格中加载的功能。
    工作簿中中原有的图表不会被加载
18、什么是冻结窗格？
    冻结特定的行，即使电子表格滚动时，冻结的部分也不会动
19、创建一个条形图，需要调用哪5个函数和方法？
    openpyxl.chart.Reference()\openpyxl.chart.Series\openpyxl.chart.Series()
    openpyxl.chart.BarChart()\chartObj,append(seriesObj)和add_chart().
