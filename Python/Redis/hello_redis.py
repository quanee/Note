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
    # String操作
    print('String 操作：')
    print('设置单个键值对：')
    r.set('name', 'pangdahai')
    print(r.get('name'))
    r.delete('name')
    print(r.get('name'))

    print('设置多个键值对：')
    r.mset(name='pangdahai', sex='male')
    print(r.mget('name', 'sex'))
    r.delete('name')
    print(r.mget('name', 'sex'))
    r.delete('sex')
    print(r.mget('name', 'sex'))


    # Hash操作
    print('Hash操作；')
    print('在hash中设置一个键值对：')
    r.hset('author', 'name', 'pangdahai')
    r.hset('author', 'sex', 'male')
    print(r.hgetall('author'))
    print(r.hget('author', 'name'))
    r.hdel('author', 'sex')
    print(r.hgetall('author'))



