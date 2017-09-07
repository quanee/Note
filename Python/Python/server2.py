import socket
import time

sk = socket.socket()
print(sk)

address = ('127.0.0.1', 8080)

sk.bind(address)  # 绑定IP和端口 1

sk.listen(3)  # 排队连接个数 2
try:
    sk.setblocking(False)
except Exception: