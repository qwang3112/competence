#-*- coding = utf-8 -*-
#@Time : 6/2/2020 9:47 AM
#@Author : John
#@File : app.py
#@Software : PyCharm

from flask import Flask, render_template
# import sqlite3
import xlrd
import numpy as np



app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

# 函数名最好和route里保持一致
@app.route('/index')
def home():
    return render_template("index.html")

@app.route('/analysis')
def analysis():

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
    # scater_list = [[x,y] for x,y in zip(competence_list, average_competence_list)]

    # 计算各个主要area的平均值
    item_list = ['G2 system','G3 system','QA Verification','Test tools','CI Machine',
                 'Troubleshooting','Programming','4G and 5G','Other skills']
    average_area_list = []
    area_list = []
    g2sys = average_competence_list[0:8]
    area_list.append(g2sys)
    g3sys = average_competence_list[8:10]
    area_list.append(g3sys)
    qa = average_competence_list[10:16]
    area_list.append(qa)
    testtool = average_competence_list[16:26]
    area_list.append(testtool)
    cimachine = average_competence_list[26:31]
    area_list.append(cimachine)
    troubleshooting = average_competence_list[31:37]
    area_list.append(troubleshooting)
    programming = average_competence_list[37:41]
    area_list.append(programming)
    fg5g = average_competence_list[41:50]
    area_list.append(fg5g)
    other = average_competence_list[50:53]
    area_list.append(other)

    for area in area_list:
        average_area = np.mean(area)
        average_area = int(average_area * 10) / 10
        average_area_list.append(average_area)



    # 可以通过col.values()按列获取数据，计算每个员工的平均值
    average_employee_list = []
    employee_list = []
    # print(cols)
    for col in range(cols):
        col_data = table.col_values(col)
        if col_data[0] != 'Competence':
            employee_list.append(col_data[0])
            col_data = col_data[1:]
            average = np.mean(col_data)
            average = int(average*10)/10
            average_employee_list.append(average)

    # 各数值分布饼状图
    count0 = 0  # 0
    count1 = 0  # 1
    count2 = 0  # 2
    count3 = 0  # 3
    count4 = 0  # 4
    count5 = 0  # 5
    for row in range(rows):
        row_data = table.row_values(row)
        if row_data[0] != 'Competence':
            row_data = row_data[1:]
            for i in range(len(row_data)):
                if row_data[i] == 0:
                    count0 = count0 + 1
                elif row_data[i] == 1:
                    count1 = count1 + 1
                elif row_data[i] == 2:
                    count2 = count2 + 1
                elif row_data[i] == 3:
                    count3 = count3 + 1
                elif row_data[i] == 4:
                    count4 = count4 + 1
                elif row_data[i] == 5:
                    count5 = count5 + 1


    per_list = [
        {'value': count0, 'name': 'level=0'},
        {'value': count1, 'name': 'level=1'},
        {'value': count2, 'name': 'level=2'},
        {'value': count3, 'name': 'level=3'},
        {'value': count4, 'name': 'level=4'},
        {'value': count5, 'name': 'level=5'}
    ]

    return render_template("analysis.html", competence_list=competence_list,
                           average_competence_list=average_competence_list, employee_list=employee_list,
                           average_employee_list=average_employee_list, per_list=per_list,
                           item_list=item_list,average_area_list=average_area_list)

@app.route('/focus')
def focus():

    return render_template("focus.html")

@app.route('/plan')
def plan():
    # 从xls文件中读取数据
    workbook = xlrd.open_workbook('plan.xlsx')
    table = workbook.sheet_by_name('Sheet1')
    rows = table.nrows
    # 可以通过row.values()按行获取数据，计算每个competence的平均值
    plans_list = []
    for row in range(rows):
        row_data = table.row_values(row)
        if row_data[0] != 'name':
            # row_data = [str(cell).replace('\n', '<br>') for cell in row_data]
            plans_list.append(row_data)

    return render_template("plan.html",plans=plans_list)

@app.route('/team')
def team():
    return render_template("team.html")


if __name__ == '__main__':
    app.run(debug=True)