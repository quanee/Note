import socket
import subprocess

sk = socket.socket()
print(sk)

address = ('127.0.0.1', 8000)

sk.bind(address)  # 绑定IP和端口 1
