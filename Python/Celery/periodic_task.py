from celery import Celery
from celery.schedules import crontab
"""通过调用函数添加定时任务定时任务"""

 
app = Celery('task', broker='redis://:password@//localhost:port', backend='redis://:password@//localhost:port')
 
@app.on_after_configure.connect