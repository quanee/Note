from concurrent.futures import ThreadPoolExecutor
import requests
import time


def task(url):
    response = requests.get(url)
    return response
    # time.sleep(1)


def done(future, *args, **kwargs):
    response = future.result()
    # print(response.content)
    print(response.status_code)


pool = ThreadPoolExecutor(5)

url_list = [