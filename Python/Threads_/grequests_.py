import grequests
'''
gevent+requests的封装
'''


request_list = [
    grequests.get('http://www.baidu.com/', timeout=0.1),
    grequests.get('http://www.bing.com/'),
    grequests.get('http://www.github.com/'),