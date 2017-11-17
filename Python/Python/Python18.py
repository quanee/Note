import requests

url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%88%90%E9%83%BD&needAddtionalResult=false&isSchoolJob=0'

data = {'first': 'false',
        'pn': 4,
        'kd': 'Python'}

header = {
          'Accept': 'application/json, text/javascript, */*; q=0.01',
          'Accept-Encoding': 'gzip, deflate, br',
          'Accept-Language': 'zh-CN,zh;q=0.9',
          'Connection': 'keep-alive',
          'Content-Length': '25',
          'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'Cookie': 'JSESSIONID=ABAAABAAAIAACBIE92228895A98B421305F0DAF84A3C480; _ga=GA1.2.2022183304.1519993626; _gid=GA1.2.1444105288.1519993626; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1519993626; user_trace_token=20180302202705-04986faf-1e15-11e8-9a2f-525400f775ce; LGSID=20180302202705-0498712f-1e15-11e8-9a2f-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGUID=20180302202705-0498747f-1e15-11e8-9a2f-525400f775ce; index_location_city=%E6%88%90%E9%83%BD; TG-TRACK-CODE=index_navigation; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1519993777; LGRID=20180302203152-af86de23-1e15-11e8-b118-5254005c3644; SEARCH_ID=f8c3ceb212334238982b24b85d0cc95e',
          'Host': 'www.lagou.com',
          'Origin': 'https://www.lagou.com',
          'Referer': 'https://www.lagou.com/jobs/list_Python?city=%E6%88%90%E9%83%BD&cl=false&fromSearch=true&labelWords=&suginput=',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',