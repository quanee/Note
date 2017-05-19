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

# 3. 等待服务端响应
data = sk.recv(8096)  # IO阻塞
print(data)

# 关闭连接
sk.close()
"""


class HttpRequest(object):
    """docstring for HttpRequest"""
    def __init__(self, sk, host, callback):
        self.socket = sk
        self.host = host
        self.callback = callback

    def fileno(self):
        return self.socket.fileno()


class HttpResponse(object):
    """docstring for HttpResponse"""
    def __init__(self, recv_data):
        self.recv_data = recv_data
        self.header_dict = {}
        self.body = None

        self.initialize()

    def initialize(self):
        headers, body = self.recv_data.split(b'\r\n\r\n', 1)
        header_list = headers.split(b'\r\n')
        for h in header_list:
            h_str = str(h, encoding='utf-8')
            v = h_str.split(':', 1)
            if len(v) == 2: