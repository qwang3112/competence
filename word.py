# #-*- coding = utf-8 -*-
# #@Time : 6/3/2020 2:48 PM
# #@Author : John
# #@File : wordcloud.py
# #@Software : PyCharm
# import jieba        #分词
# import xlrd
# from matplotlib import pyplot as plt    #绘图，数据可视化
# from wordcloud import WordCloud         #词云
# from PIL import Image                   #图片处理
# import numpy as np                      #矩阵运算
# import sqlite3                          #数据库
#
#
# #准备词云所需的文字（词）
#
# # con = sqlite3.connect('movie.db')
# # cur = con.cursor()
# # sql = 'select instroduction from movie250'
# # data = cur.execute(sql)
# # text = ""
# # for item in data:
# #     text =  text + item[0]
# #     #print(item[0])
# # #print(text)
# # cur.close()
# # con.close()
#
# # 从xls文件中读取数据
# workbook = xlrd.open_workbook('competence.xlsx')
# # print(workbook)
# # 可以使用workbook对象的sheet_names()方法获取到excel文件中哪些表有数据
# # print(workbook.sheet_names())
# # 可以通过sheet_by_index()方法或sheet_by_name()方法获取到一张表，返回一个对象
# # table = workbook.sheet_by_index(0)
# # print(table)
# table = workbook.sheet_by_name('Sheet1')
# # print(table)
# # 通过nrows和ncols获取到表格中数据的行数和列数
# rows = table.nrows
# cols = table.ncols
# employee_list = []
# competence_list = []
# for row in range(rows):
#     row_data = table.row_values(row)
#     if row_data[0] == 'Competence':
#         employee_list = row_data[1:]
#     competence_list.append(row_data[0])
#
# text = ''
# for item in employee_list:
#     text = text + item[0]
# for item in competence_list:
#     text = text + item[0]
#
# #分词
# cut = jieba.cut(text)
# string = ' '.join(cut)
# # print(len(string))
#
#
# img = Image.open(r'.\static\assets\img\tree.jpg')   #打开遮罩图片
# img_array = np.array(img)   #将图片转换为数组
# wc = WordCloud(
#     background_color='white',
#     mask=img_array,
#     font_path="msyh.ttc"    #字体所在位置：C:\Windows\Fonts
# )
# wc.generate_from_text(string)
#
#
# #绘制图片
# fig = plt.figure(1)
# plt.imshow(wc)
# plt.axis('off')     #是否显示坐标轴
#
# # plt.show()    #显示生成的词云图片
#
# #输出词云图片到文件
# plt.savefig(r'.\static\assets\img\word.jpg', dpi=500)