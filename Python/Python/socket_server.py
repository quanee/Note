import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print("服务启动...")
        while True:
            conn = self.request