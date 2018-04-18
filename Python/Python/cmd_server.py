import socket
import subprocess

sk = socket.socket()
print(sk)

address = ('127.0.0.1', 8000)

sk.bind(address)  # 绑定IP和端口 1

sk.listen(3)  # 排队连接个数 2

while True:
    conn, addr = sk.accept()
    print(addr)
    while True:
        try:
            data = conn.recv(1024)
        except Exception:
            break
        if not data:
            break
        print(str(data, 'utf8'))

        # subprocess.PIPE 将子进程输出转到主进程
        obj = subprocess.Popen(str(data, 'utf8'), shell=True, stdout=subprocess.PIPE)
        cmd_result = obj.stdout.read()
        result_len = bytes(str(len(cmd_result)), 'utf8')