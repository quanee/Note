from celery import Celery
from celery.schedules import crontab
"""通过调用函数添加定时任务定时任务"""

 
app = Celery('task', broker='redis://:password@//localhost:port', backend='redis://:password@//localhost:port')
 
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # 每10秒中调用test('hello')
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')
 
    # 每30秒中调用test('world')
    sender.add_periodic_task(30.0, test.s('world'), expires=10)