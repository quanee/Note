'''异常'''
try:
    raise Exception('主动触发异常')
    i = int('adfa')
except Exception as e: