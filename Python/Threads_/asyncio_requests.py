import asyncio
import requests
'''
asyncio配合requests
asyncio 实现IO异步
requests 实现封装Http数据包
'''


@asyncio.coroutine
def fetch_async(func, *args):
    loop = asyncio.get_event_loop()
    future = loop.run_in_executor(None, func, *args)
    response = yield from future
    print(response.url, response.content)