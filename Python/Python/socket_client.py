import socket

ip_port = ('127.0.0.1', 8091)
sk = socket.socket()
sk.connect(ip_port)
print('客户端启动:')

while True:
    inp = input('>>>')
    sk.sendall(bytes(inp, 'utf8'))