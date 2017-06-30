'''
MySQL-Python
    mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>

pymysql
    mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]

MySQL-Connector
    mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>

cx_Oracle
    oracle+cx_oracle://user:pass@host:port/dbname[?key=value&key=value...]
'''

#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy import create_engine


engine = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/t1", max_overflow=5)

# 执行SQL
# cur = engine.execute(
#     "INSERT INTO hosts (host, color_id) VALUES ('1.1.1.22', 3)"
# )

# 新插入行自增ID
# cur.lastrowid

# 执行SQL
# cur = engine.execute(
#     "INSERT INTO hosts (host, color_id) VALUES(%s, %s)",[('1.1.1.22', 3),('1.1.1.221', 3),]
# )


# 执行SQL
# cur = engine.execute(
#     "INSERT INTO hosts (host, color_id) VALUES (%(host)s, %(color_id)s)",
#     host='1.1.1.99', color_id=3
# )

# 执行SQL
# cur = engine.execute('select * from hosts')
# 获取第一行数据
# cur.fetchone()