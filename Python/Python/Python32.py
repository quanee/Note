#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pymysql
'''
pymysql操作
'''
# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='t1')
# 创建游标
cursor = conn.cursor()

# 执行SQL，并返回收影响行数
effect_row = cursor.execute("update hosts set host = '1.1.1.2'")

# 执行SQL，并返回受影响行数
# effect_row = cursor.execute("update hosts set host = '1.1.1.2' where nid > %s", (1,))

# 执行SQL，并返回受影响行数
# effect_row = cursor.executemany("insert into hosts(host,color_id)values(%s,%s)", [("1.1.1.11",1),("1.1.1.11",2)])

# 获取第一行数据
row_1 = cursor.fetchone()

# 获取前n行数据