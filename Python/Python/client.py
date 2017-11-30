import socket

sk = socket.socket()
print(sk)

address = ('127.0.0.1', 8000)

sk.connect(address)  # 连接服务端 1

'''