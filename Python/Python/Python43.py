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