'''
time模块
random模块
os模块
sys模块
hashlib模块
logging模块
'''



import time

print(time.clock())  # 返回处理器时间,3.3开始已废弃 , 改成了time.process_time()测量处理器运算时间,不包括sleep时间,不稳定,mac上测不出来
print(time.altzone)  # 返回与utc时间的时间差,以秒计算\
print(time.asctime())  # 返回时间格式'Fri Aug 19 11:14:16 2016',
print(time.localtime())  # 返回本地时间 的struct time对象格式
print(time.gmtime(time.time() - 800000))  # 返回utc时间的struc时间对象格式

print(time.asctime(time.localtime()))  # 返回时间格式'Fri Aug 19 11:14:16 2016',
print(time.ctime())  # 返回Fri Aug 19 12:38:29 2016 格式, 同上