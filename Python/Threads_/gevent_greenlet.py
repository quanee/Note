from gevent import monkey
from gevent.pool import Pool
monkey.patch_all()
import gevent
import requests
'''gevent(协程)+requests(请求)'''
