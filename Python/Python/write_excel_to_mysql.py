import xlrd

import sqlite3

file = "H:\\xls\\全国省市县列表.xls"

data = xlrd.open_workbook(file)

table = data.sheets()[0]  # 第一个sheets

datalist = []

for i in range(1, table.nrows):  # 总行数