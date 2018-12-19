import redis
from error import PoolEmptyError
from setting import REDIS_HOST, REDIS_KEY, REDIS_PASSWORD, REDIS_PORT
from setting import MAX_SCORE, MIN_SCORE, INITIAL_SCORE
from random import choice
import re

class RedisClient():
    def __init__(self, host = REDIS_HOST, port = REDIS_PORT, password = REDIS_PASSWORD):
        """
        初始化
        :param host: redis 地址
        :param port: redis 端口
        :param password: redis 密码
        """
        # 连接redis，加上decode_responses=True，写入的键值对中的value为str类型，不加这个参数写入的则为字节类型。
        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)
    
    def add(self, proxy, score = INITIAL_SCORE):
        """
        添加代理，设置分数为最高
        :param proxy: 代理
        :param score: 分数
        :return: 添加结果
        """        
        if not re.match(r'\d+\.\d+\.\d+\.\d+\:\d+', proxy):
            print('代理不合规范！ ', proxy, ' 丢弃！')
            return
        if not self.db.zscore(REDIS_KEY, proxy):
            return self.db.zadd(REDIS_KEY, {proxy:score})

if  __name__ == '__main__':
    conn = RedisClient()
    result = conn.add('192.168.8.2:8888')
    print(result)