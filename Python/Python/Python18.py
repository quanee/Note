import requests

url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%88%90%E9%83%BD&needAddtionalResult=false&isSchoolJob=0'

data = {'first': 'false',
        'pn': 4,
        'kd': 'Python'}

header = {
          'Accept': 'application/json, text/javascript, */*; q=0.01',
          'Accept-Encoding': 'gzip, deflate, br',
          'Accept-Language': 'zh-CN,zh;q=0.9',