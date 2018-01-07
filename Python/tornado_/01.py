# coding: utf-8
import tornado.web
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    """主页处理类"""
    def get(self):
        """get请求方式"""
        self.write('hello tornado')


if __name__ == '__main__':
    app = tornado.web.Application([('/', IndexHandler)])
    app.listen(8000)