import xlrd

import sqlite3

file = "H:\\xls\\全国省市县列表.xls"

data = xlrd.open_workbook(file)

table = data.sheets()[0]  # 第一个sheets

datalist = []

for i in range(1, table.nrows):  # 总行数

    datalist.append(tuple(table.row_values(i)))

conn = sqlite3.connect('d:\\database\\country.db')  # 数据库文件的路径

cursor = conn.cursor()

cursor.execute("create table country(province varchar(20),num int,town varchar(30),town varchar(30))")  # #创建表

sql = 'insert into country(province,num,city,town) values(?,?,?,?)'

cursor.executemany(sql, datalist)  # 插入数据
