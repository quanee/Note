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

conn.commit()  # 提交数据到数据库

conn.close()  # 关闭连接

print("导入完成")
# 将excel导入mysql
#/usr/bin/env python3

# -*- coding:utf-8 -*-

import os
import sys
import getopt
import openpyxl
import pymysql
import datetime
import re
import itertools

# 数据库连接配置文件

__db_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'your.db.username',
    'password': 'your.db.password',
    'db': 'xls',
    'charset': 'utf8'
}

####################


def usage():

    print('xls2db.py usage:')

    print(' xls2db filename(xlsx)')
