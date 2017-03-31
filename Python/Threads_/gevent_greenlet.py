from gevent import monkey
from gevent.pool import Pool
monkey.patch_all()
import gevent
import requests
'''gevent(协程)+requests(请求)'''



def task(method, url, req_kwargs):
    print(method, url, req_kwargs)
    response = requests.request(method=method, url=url, **req_kwargs)
    print(response.url, response.content)


# 发送请求 (一次全部发送)
# gevent.joinall([
#       gevent.spawn(task, method='get', url='http://www.baidu.com/', req_kwargs={}),
#       gevent.spawn(task, method='get', url='http://www.bing.com/', req_kwargs={}),
#       gevent.spawn(task, method='get', url='http://www.sougou.com/', req_kwargs={}),
#     ])