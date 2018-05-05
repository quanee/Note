from concurrent.futures import ProcessPoolExecutor
from multiprocessing import freeze_support
import requests
import time


def task(url):
    response = requests.get(url)
    return response
    # time.sleep(1)


def done(future, *args, **kwargs):
    response = future.result()
    # print(response.content)
    print(response)
    print(response.status_code)


pool = ProcessPoolExecutor(8)

url_list = [
    'http://www.baidu.com',
    'http://www.bing.com',
    'http://www.zhihu.com',
    'http://www.sina.com',
    'http://www.youku.com',
    'http://www.toutiao.com',
]
