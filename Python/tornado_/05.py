# coding:utf-8

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

from tornado.options import define, options
from tornado.web import RequestHandler, url

tornado.options.define('port', type=int, default=8888, help='服务器端口')


class IndexHandler(RequestHandler):
    """主页处理类"""
    def get(self):
        """get请求方式"""
        # self.write('<a href="'+self.reverse_url('cpp_url') + '">cpp</a>')