import subprocess

from celery import Celery
"""
定时任务
启动:
    $ celery -A task worker --loglevel=info
    $ python
    >>> from task import add
    >>> from task import run_cmd
    >>> add.delay(x, y)
    >>> r = run_cmd.delay('ls')
    >>> print(r)
"""


# app = Celery('tasks', broker='redis://localhost', backend='redis://localhost')

app = Celery('task', broker='redis://:moonboss@localhost:port', backend='redis://:password@localhost:port')


@app.task
def add(x, y):
    print('running...', x, y)
    return x + y

