from tornado.httpclient import AsyncHTTPClient
from tornado.httpclient import HTTPRequest
from tornado import ioloop


COUNT = 0
def handle_response(response):
    """处理返回值内容(（)需要维护计数器，来停止IO循环),调用 ioloop.IOLoop.current().stop()"""
    global COUNT
    COUNT -= 1
    if response.error:
        print("Error:", response.error)
    else:
        # print(response.body)
        print('response.url')

    if COUNT == 0:
        ioloop.IOLoop.current().stop()