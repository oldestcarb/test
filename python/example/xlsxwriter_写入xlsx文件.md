### xlsxwriter写入xlsx文件
```python

import xlsxwriter
from xlsxwriter.exceptions import DuplicateWorksheetName

def write_excel(self, sheet, result):
    """
    向excel中写入数据
    :params sheet: 疾病名字，表名
    :params result: 数据列表
    """
    # excel文件路径
    infile = 'C:/Users/CRAB/Desktop/右边分类.xlsx'
    # 打开一个xlsx文件（如果打开的文件存在 ，则清空该文件，如果文件不存在，则新建）
    workbook = xlsxwriter.Workbook(infile)
    try:
        sheet = workbook.add_worksheet(sheet)
    # 避免重名
    except DuplicateWorksheetName:
        sheet = workbook.add_worksheet(sheet+'(1)')
    # 写入字段名
    field_name = ['id', 'disease_source', 'GeneSymbol', 'Disease', 'PubMed_ID', 'Sentence', 'judge', 'result']
    for i in range(len(field_name)):
        sheet.write(0, i, field_name[i])

    rows = len(result)
    cols = len(result[0])
    # print(rows, cols)
    for i in range(rows):
        for j in range(cols):
            # 第一行已写入字段名
            sheet.write(i+1, j, result[i][j])

    # 关闭excel文件
    workbook.close()
```