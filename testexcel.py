#-*- coding = utf-8 -*-
#@Time : 6/12/2020 3:58 PM
#@Author : John
#@File : testexcel.py
#@Software : PyCharm
import xlrd
import numpy as np

# # 从xls文件中读取数据
# workbook = xlrd.open_workbook('competence.xlsx')
# print(workbook)
# # 可以使用workbook对象的sheet_names()方法获取到excel文件中哪些表有数据
# print(workbook.sheet_names())
# # 可以通过sheet_by_index()方法或sheet_by_name()方法获取到一张表，返回一个对象
# # table = workbook.sheet_by_index(0)
# # print(table)
# table = workbook.sheet_by_name('Sheet1')
# # print(table)
# # 通过nrows和ncols获取到表格中数据的行数和列数
# rows = table.nrows
# cols = table.ncols
#
# per_list = []
# count1 = 0 #<3
# count2 = 0 #3<=x<=4
# count3 = 0 #4<x<5
# for row in range(rows):
#     row_data = table.row_values(row)
#     if row_data[0] != 'Competence':
#         row_data = row_data[1:]
#         for i in range(len(row_data)):
#             if row_data[i] < 3:
#                 count1 = count1 + 1
#             elif 3<=row_data[i] <= 4:
#                 count2 = count2 + 1
#             elif 4<row_data[i]<=5:
#                 count3 = count3 + 1
#
# per_list = [
#                 {'value': count1, 'name': 'x<3'},
#                 {'value': count2, 'name': '3<=x<=4'},
#                 {'value': count3, 'name': '4<x<=5'},
#             ]
#
# print(per_list)
# 可以通过row.values()按行获取数据，返回一个列表，也可以按列
# average_competence_list = []
# competence_list = []
# for row in range(rows):
#     row_data = table.row_values(row)
#     # print(row_data)
#     sum = 0
#
#     if row_data[0] != 'Competence':
#         competence_list.append(row_data[0])
#         for i in range(len(row_data)):
#             if i != 0:
#                 sum += row_data[i]
#         average = sum/(len(row_data)-1)
#         average_competence_list.append(average)

# average_employee_list = []
# employee_list = []
# print(cols)
# for col in range(cols):
#     col_data = table.col_values(col)
#     print(col_data)
#     sum = 0
#
#     if col_data[0] != 'Competence':
#         employee_list.append(col_data[0])
#         for i in range(len(col_data)):
#             if i != 0:
#                 sum += col_data[i]
#         average = sum/(len(col_data)-1)
#         average_employee_list.append(average)
# print(average_employee_list)
# print(employee_list)

# 从xls文件中读取数据
# workbook = xlrd.open_workbook('plan.xlsx')
# # table = workbook.sheet_by_name('Sheet1')
# # rows = table.nrows
# # # print(rows)
# # # 可以通过row.values()按行获取数据，计算每个competence的平均值
# # plans_list = []
# # for row in range(rows):
# #     row_data = table.row_values(row)
# #     row_data = [str(cell).replace('\n','<br>') for cell in row_data]
# #     plans_list.append(row_data)
# #
# # print(plans_list)

# 从xls文件中读取数据
workbook = xlrd.open_workbook('competence.xlsx')
# print(workbook)
# 可以使用workbook对象的sheet_names()方法获取到excel文件中哪些表有数据
# print(workbook.sheet_names())
# 可以通过sheet_by_index()方法或sheet_by_name()方法获取到一张表，返回一个对象
# table = workbook.sheet_by_index(0)
# print(table)
table = workbook.sheet_by_name('Sheet1')
# print(table)
# 通过nrows和ncols获取到表格中数据的行数和列数
rows = table.nrows
cols = table.ncols
# 可以通过row.values()按行获取数据，计算每个competence的平均值
average_competence_list = []
competence_list = []
for row in range(rows):
    row_data = table.row_values(row)

    if row_data[0] != 'Competence':
        competence_list.append(row_data[0])
        row_data = row_data[1:]
        average = np.mean(row_data)
        # 保留小数点后一位
        average = int(average*10)/10
        average_competence_list.append(average)

# 散点图
scater_list = [[x,y] for x,y in zip(competence_list, average_competence_list)]
print(scater_list)
