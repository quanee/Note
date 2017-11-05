from concurrent.futures import ThreadPoolExecutor
import requests
import time


def task(url):
    response = requests.get(url)
    return response
    # time.sleep(1)
