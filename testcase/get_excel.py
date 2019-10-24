# coding:utf-8

"""
@project : jiekou
@author  : 三十
@file   : get_excel.py  读取Excel
@ide    : PyCharm
@time   : 2019-06-17 10:45:16
"""
import xlrd
import json
#读取 Excel表中的数据
def configExcel(xls_name='test_case.xlsx',sheet_index=0):

    cls = [] #定义一个空列表 用来接收 每行的数据
    xls_open = xlrd.open_workbook(xls_name,encoding_override='utf-8')# 打开Excel表
    sheet = xls_open.sheet_by_index(sheet_index) #根据 sheet对象来获取那个表
    nrows = sheet.nrows  #获取所有的行
    for row in range(1,nrows):   #遍历 所有的 行
        cls.append(sheet.row_values(row))  # 把每行的数据添加到cls 列表里面

    # print(cls[0])
    # print(cls[1])
    return cls   # 调用这个函数得到这个表中的所有行的数据


if __name__ == '__main__':
    f = configExcel()
