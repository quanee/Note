import asyncio
'''
协程: (微线程) + 异步IO
      一个线程 发送多个请求
无法发送Http协议
只能发送TCP协议
'''


@asyncio.coroutine
def task(host, url='/'):
    reader, writer = yield from asyncio.open_connection(host, 80)
    request_header_content = '''GET %s HTTP/1.0\r\nHost: %s\r\n\r\n''' % (url, host, )
    request_header_content = bytes(request_header_content, encoding='utf-8')
