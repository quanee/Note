import socket
import subprocess

sk = socket.socket()
print(sk)

address = ('127.0.0.1', 8000)

sk.bind(address)  # 绑定IP和端口 1

sk.listen(3)  # 排队连接个数 2

while True:
    conn, addr = sk.accept()
    print(addr)
    while True:
        try:
            data = conn.recv(1024)
        except Exception:
            break