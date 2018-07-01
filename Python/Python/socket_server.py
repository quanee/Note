import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print("服务启动...")
        while True:
            conn = self.request
            print(self.client_address)
            while True:
                client_data = conn.recv(1024)
                print(str(client_data, 'utf8'))

                print('waiting...')
                server_response = input('>>>')
                conn.sendall(bytes(server_response, 'utf8'))
            conn.close()
