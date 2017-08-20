import socket

'''
网络编程
--------------------------------------------------------------------
流程描述：
1 服务器根据地址类型（ipv4,ipv6）、socket类型、协议创建socket
2 服务器为socket绑定ip地址和端口号
3 服务器socket监听端口号请求，随时准备接收客户端发来的连接，这时候服务器的socket并没有被打开
4 客户端创建socket
5 客户端打开socket，根据服务器ip地址和端口号试图连接服务器socket
6 服务器socket接收到客户端socket请求，被动打开，开始接收客户端请求，直到客户端返回连接信息。这时候socket进入阻塞状态，所谓阻塞即accept()方法一直等到客户端返回连接信息后才返回，开始接收下一个客户端连接请求
7 客户端连接成功，向服务器发送连接状态信息
8 服务器accept方法返回，连接成功
9 客户端向socket写入信息(或服务端向socket写入信息)
10 服务器读取信息(客户端读取信息)
11 客户端关闭
12 服务器端关闭
--------------------------------------------------------------------
'''
'''
SOCK_STREAM:TCP
SOCK_DGRAM :UDP
family = AF_INET : 服务器之间的通信
family = AF_INET6: 服务器之间的通信
family = AF_UNIX : Unix不同进程间通信

sk.bind(address)    #将套接字绑定到地址。address地址的格式取决于地址族。在AF_INET下，以元组（host,port）的形式表示地址。
sk.listen(backlog)  #开始监听传入连接。backlog指定在拒绝连接之前，可以挂起的最大连接数量。
                    #backlog等于5，表示内核已经接到了连接请求，但服务器还没有调用accept进行处理的连接个数最大为5
                    #这个值不能无限大，因为要在内核中维护连接队列
sk.setblocking(bool)    #是否阻塞（默认True），如果设置False，那么accept和recv时一旦无数据，则报错。
sk.accept()             #接受连接并返回（conn,address）,其中conn是新的套接字对象，可以用来接收和发送数据。address是连接客户端的地址。
                        #接收TCP 客户的连接（阻塞式）等待连接的到来
sk.connect(address)     #连接到address处的套接字。一般，address的格式为元组（hostname,port）,如果连接出错，返回socket.error错误。
sk.connect_ex(address)  #同上，只不过会有返回值，连接成功时返回 0 ，连接失败时候返回编码，例如：10061
sk.close()  #关闭套接字
sk.recv(bufsize[,flag])     #接受套接字的数据。数据以字符串形式返回，bufsize指定最多可以接收的数量。flag提供有关消息的其他信息，通常可以忽略。
sk.recvfrom(bufsize[.flag]) #与recv()类似，但返回值是（data,address）。其中data是包含接收数据的字符串，address是发送数据的套接字地址。
sk.send(string[,flag])      #将string中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于string的字节大小。即：可能未将指定内容全部发送。
sk.sendall(string[,flag])   #将string中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。成功返回None，失败则抛出异常。
                            #内部通过递归调用send，将所有内容发送出去。
sk.sendto(string[,flag],address)  #将数据发送到套接字，address是形式为（ipaddr，port）的元组，指定远程地址。返回值是发送的字节数。该函数主要用于UDP协议。
sk.settimeout(timeout)  #设置套接字操作的超时期，timeout是一个浮点数，单位是秒。值为None表示没有超时期。一般，超时期应该在刚创建套接字时设置，因为它们可能用于连接的操作（如 client 连接最多等待5s ）
sk.getpeername()  #返回连接套接字的远程地址。返回值通常是元组（ipaddr,port）。
sk.getsockname()  #返回套接字自己的地址。通常是一个元组(ipaddr,port)
sk.fileno()  #套接字的文件描述符

'''