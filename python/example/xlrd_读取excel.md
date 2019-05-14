#### 读取excel
```python
# -*- coding:utf-8 -*-

import time
import xlrd
import pymysql

def read_excel(infile):
    """
    读取excel文件
    :params infile: excel文件路径
    """
    # 获取文件
    excel_file = xlrd.open_workbook(infile)
    # 获取sheet名
    print(excel_file.sheet_names())
    # ['array_list_new', 'Sheet1']

    # 获取sheet内容
    sheet = excel_file.sheet_by_index(0)
    # sheet = excel_file.sheet_by_name('array_list_new')
    print(sheet)
    # <xlrd.sheet.Sheet object at 0x0000029F479EAE10>

    # 获取sheet名称、行数、列数
    print(sheet.name, sheet.nrows, sheet.ncols)
    # array_list_new 514 13

    # 获取第三行和第二列的值
    rows = sheet.row_values(2)
    cols = sheet.col_values(1)
    # print(rows, cols)



if __name__ == "__main__":
    print('start', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    start = time.time()

    # infile = r'C:/Users/CRAB/Desktop/gene_disease/数据校对 5.9 array_list_new.xlsx'
    infile = r'C:/Users/CRAB/Desktop/gene_disease/gene_symbol.xlsx'
    read_excel(infile)

    print('stop', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    print('all', time.time()-start)
```
