import socket
import os
'''文件上传客户端'''


sk = socket.socket()
print(sk)

address = ('127.0.0.1', 8000)

sk.connect(address)  # 连接服务端 1

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while True:
    inp = input('>>>').strip()  # post|18000.jpg

    cmd, path = inp.split('|')

    os.path.join(BASE_DIR, path)