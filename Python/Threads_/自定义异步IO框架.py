import socket
import select

"""
# ################# HTTP请求本质 阻塞 ################### 
sk = socket.socket()
# 1. 连接
sk.connect(('www.baidu.com', 80, ))  # IO阻塞
print('连接成功...')

# 2. 发送消息
sk.send(b'GET /index HTTP/1.0\r\nHost: baidu.com\r\n\r\n')
# sk.send(b'POST /index HTTP/1.0\r\nHost: baidu.com\r\n\r\nk1=v1?k2=v2')

# 3. 等待服务端响应
data = sk.recv(8096)  # IO阻塞
print(data)

# 关闭连接
sk.close()

"""
"""
sk = socket.socket()
sk.setblocking(False)
# 1. 连接
try:
    sk.connect(('www.baidu.com', 80, ))  # IO阻塞
    print('连接成功...')
except Exception as e:
    print(e)

# 2. 发送消息
sk.send(b'GET /index HTTP/1.0\r\nHost: baidu.com\r\n\r\n')
# sk.send(b'POST /index HTTP/1.0\r\nHost: baidu.com\r\n\r\nk1=v1?k2=v2')
