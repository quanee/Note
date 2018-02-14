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