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
        # subjects = self.get_query_arguments('subject')
        # self.write(str(subjects))
        # subject = self.get_query_argument('subject')
        # self.write(subject)
        # body_arg = self.get_body_argument('b')
        # body_args = self.get_body_arguments('b')
        # a = self.get_argument('a')
        # ags = self.get_arguments('a')
        # self.write(str(ags))

    def post(self):
        # a = self.get_argument('a')
        # ags = self.get_arguments('a')
        # body_arg = self.get_body_argument('b')
        # body_args = self.get_body_arguments('b')
        # self.write(str(body_args))
        print(type(self.request.files))
        print(self.request.files.keys())
        print(type(self.request.files['img1']))
        with open('img.jpg', 'wb') as f:
            f.write(self.request.files['img1'][0]['body'])
        self.write('ok')

