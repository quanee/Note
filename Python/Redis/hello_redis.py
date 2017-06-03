import redis
import datetime

# 管理对redis的所有连接，避免每次建立，释放连接的开销
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
# Redis实例
r = redis.Redis(connection_pool=pool)

r.set("testbin", 0b1111)
print(r.get("testbin"))
print(bin(int(r.get("testbin"))))

start = datetime.datetime.now()
# for i in range(1, 1000000):
    # r.set(i, i)
end = datetime.datetime.now()
print(end - start)


if __name__ == '__main__':