'''IO多路复用'''


# 客户端
"""
try:
    socket_obj_1.connet()
    socket_obj_2.connet()
    socket_obj_3.connet()
except Exception:
    ...


while True:
    r, w, e = select.select([socket_obj_1, socket_obj_2, socket_obj_3, ], [socket_obj_1, socket_obj_2, socket_obj_3, ], [], 0.05)
    r = [socket_obj_1, ]  # 2对方发数据
        xx = socket_obj_1.recv()  # 4

    w = [socket_obj_1, ]  # 1与对方创建连接成功
        socket_obj_1.send("'''GET /index HTTP/1.0\r\nHost: baidu.com\r\n\r\n'''")  # 3

# $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $

r, w, e = select.select([obj], [], [])
# obj 可以不是socket对象 但必须有fileno方法 并返回一个文件描述符
# select内部:
#       * 调用 obj.fileno()方法
#       * obj类内部封装socket文件描述符
"""
