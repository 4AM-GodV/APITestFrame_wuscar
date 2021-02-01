import os
import xlrd
from common.excel_utils import ExcelUtils


excel_path = os.path.join( os.path.dirname(__file__), 'data/ko.xlsx')
excelUtils = ExcelUtils(excel_path, "Sheet1")
# print(excelUtils.get_merged_cell_value(8, 0))
sheet_list = []
for row in range(1, excelUtils.get_row_count()):
    row_dict = {}
    row_dict["事件"] = excelUtils.get_merged_cell_value(row, 0)
    row_dict["步骤序号"] = excelUtils.get_merged_cell_value(row, 1)
    row_dict["步骤操作"] = excelUtils.get_merged_cell_value(row, 2)
    row_dict["完成情况"] = excelUtils.get_merged_cell_value(row, 3)
    sheet_list.append(row_dict)

# for row in sheet_list:
#     print(row)


alldata_list = []
first_row = excelUtils.sheet.row(0)
for row in range(1, excelUtils.get_row_count()):
    row_dict = {}
    for col in range(0, excelUtils.get_col_count()):
        row_dict[first_row[col].value] = excelUtils.get_merged_cell_value(row, col)
    alldata_list.append(row_dict)

for row in alldata_list:
    print(row)






