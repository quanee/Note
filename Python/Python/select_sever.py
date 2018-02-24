import socket
import select


sk1 = socket.socket()
address = ('127.0.0.1', 8080)
sk1.bind(address)
sk1.listen(3)

sk2 = socket.socket()
address = ('127.0.0.1', 8081)