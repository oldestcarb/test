import redis


pool = redis.ConnectionPool(host='127.0.0.1', port=6379)

conn = redis.StrictRedis(connection_pool=pool)
a = conn.zadd('proxies', {'111.1.1':1111})
print(a)