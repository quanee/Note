import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print("服务启动...")