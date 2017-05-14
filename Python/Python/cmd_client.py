import socket

sk = socket.socket()
print(sk)

address = ('127.0.0.1', 8000)

sk.connect(address)  # 连接服务端 1

'''

'''
while True:
    inp = input('>>>')
    if inp == 'exit':
        break
    sk.send(bytes(inp, 'utf8'))
    # 接受字符长度
    result_len = int(str(sk.recv(1024), 'utf8'))
    print(result_len)
