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

    filename = os.path.basename(path)
    file_size = os.stat(path).st_size

    file_info = 'post|%s|%s' % (filename, file_size)

    sk.sendall(bytes(file_info, 'utf8'))

    has_send = 0
    f = open(path, 'rb')
    # with open(path, 'rb') as f:
    while has_send != file_size:
        data = f.read(1024)
        sk.sendall(data)
        has_send += len(data)