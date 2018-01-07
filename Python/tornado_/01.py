# coding: utf-8
import tornado.web
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    """主页处理类"""
    def get(self):
        """get请求方式"""
        self.write('hello tornado')
