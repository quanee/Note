import socket
import os
'''文件上传服务器端'''


sk = socket.socket()
print(sk)

address = ('127.0.0.1', 8000)

sk.bind(address)  # 绑定IP和端口 1

sk.listen(3)  # 排队连接个数 2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while True:
    conn, addr = sk.accept()
    print(addr)
    while True:
        data = conn.recv(1024)
        cmd, filename, filesize = str(data, 'utf8').split('|')
        path = os.path.join(BASE_DIR, '__pycache__', filename)
        filesize = int(filesize)

        f = open(path, 'ab')
