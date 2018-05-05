from concurrent.futures import ProcessPoolExecutor
from multiprocessing import freeze_support
import requests
import time


def task(url):
    response = requests.get(url)
    return response
    # time.sleep(1)

