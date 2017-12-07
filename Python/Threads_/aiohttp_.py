import aiohttp
import asyncio
'''aiohttp 封装http协议'''


@asyncio.coroutine
def fetch_async(url):
    print(url)
    response = yield from aiohttp.request('GET', url)
    print(url, response)
    response.close()


tasks = [
         fetch_async('http://www.baidu.com'),