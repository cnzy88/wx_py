#coding: utf-8
import redis

class RedisOperate(object):

    def __init__(self, db=0, ip='127.0.0.1', port=6379):
        self.client = redis.Redis(
            connection_pool=redis.BlockingConnectionPool(max_connections=15, host=ip, port=port, db=db))

    def get(self, k):
        """
        获取类型为string的值
        :param k:
        :return:
        """
        return self.client.get(k)

    def set(self, k, v, ex=None):
        """
        设置string类型的值
        :param k:
        :param v:
        :param ex:
        :return:
        """
        self.client.set(k, v, ex=ex)

    def hget(self, name, k=None):
        """
        获取hash类型的某个字段的值
        :param name:
        :param k:
        :return:
        """
        if k:
            return self.client.hget(name, k)
        else:
            return self.client.hgetall(name)

    def hset(self, name, obj):
        """
        设置hash类型的所有k-v对
        :param obj:
        :return:
        """
        for (k,v) in obj.items():
            self.client.hset(name, k, v)

    def lpush(self, name, l):
        """
        存数组(元素不能是对象)
        :param name:
        :param l:
        :return:
        """
        self.client.lpushx(name, *l)

if __name__ == '__main__':
    redis_operate = RedisOperate(db=1)
    # print redis_operate.get_string('test_key')
    o = [{'c':1}, {'c':1}]
    redis_operate.lpush('test2', o)