import os

import xlrd

excel_path = os.path.join( os.path.dirname(__file__), 'data/ko.xlsx')
print(excel_path)


wb = xlrd.open_workbook(excel_path)
sheet = wb.sheet_by_name("Sheet1")
# cell_value = sheet.cell_value(2, 2)
# print(cell_value)
cell_value = sheet.cell_value(1, 0)
print(str(cell_value))

print(sheet.merged_cells)   # 返回一个列表 起始行 结束行  起始列  结束列; 前开后必

# 凡是在属性范围内的合并单元格，它的值都要等于左上角首个单元格的值
#
# nrows = sheet.nrows
# ncols = sheet.ncols
# print(nrows, ncols)
# merged = sheet.merged_cells
# for row_index in (0, nrows):
#     for col_index in (0, ncols):
#         for (rlow, rhigh, clow, chigh) in merged:  # 遍历表格中所有合并单元格位置信息
#             if (row_index >= rlow and row_index < rhigh):  # 行坐标判断
#                 if (col_index >= clow and col_index < chigh):  # 列坐标判断
#                     # 如果满足条件，就把合并单元格第一个位置的值赋给其它合并单元格
#                     cell_value = sheet.cell_value(rlow,clow)
# print(cell_value)

merged = sheet.merged_cells
def get_merged_cell_value(row_index, col_index):
    cell_value = None
    for (rlow, rhigh, clow, chigh) in merged:  # 遍历表格中所有合并单元格位置信息
        if (row_index >= rlow and row_index < rhigh):
            if (col_index >= clow and col_index < chigh):
                cell_value = sheet.cell_value(rlow,clow)
                break;  # 防止循环去进行判断出现值被覆盖的情况
            else:
                cell_value = sheet.cell_value(row_index, col_index)
        else:
            cell_value = sheet.cell_value(row_index, col_index)
    return cell_value

print(get_merged_cell_value(3,1))

for i in range(1, 5):
    print(get_merged_cell_value(i, 0))



























