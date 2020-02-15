#coding: utf-8
import os
import requests
from wechat.exception import NotAccessTokenException
from config import WECHAT_CONF
from utils.db_redis import RedisOperate
from config import WX_ACCESS_TOKEN_STORE_WAY

class WxBaseService(object):

    #获取accessToken的地址
    GET_ACCESS_TOKEN_URL = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={0}&secret={1}'
    ACCESS_TOKEN_REDIS_KEY = 'access_token_{0}'
    ACCESS_TOKEN_FILENAME = 'access_token_{0}.txt'

    def __init__(self, appid):
        self.appid = appid
        self.access_token = self.get_access_token()

    def _store_access_token(self, way):
        """
        存储access_token到本地
        :param way: 存储方式.  1:redis   2:file
        :return:
        """
        if way == 1:
            self.redis = RedisOperate(db=0)
            self.redis.set(self.ACCESS_TOKEN_REDIS_KEY.format(self.appid), self.access_token, 7200)
        elif way == 2:
            with open(self.ACCESS_TOKEN_FILENAME.format(self.appid), 'w') as f:
                f.write(self.access_token)

    def _get_local_access_token(self, way):
        """
        从本地获取access_token
        :param way: 存储方式.  1:redis   2:file
        :return:
        """
        if way == 1:
            self.redis = RedisOperate(db=0)
            return self.redis.get(self.ACCESS_TOKEN_REDIS_KEY.format(self.appid))
        elif way == 2:
            try:
                with open(self.ACCESS_TOKEN_FILENAME.format(self.appid), 'r') as f:
                    content = f.read()
            except:
                content = None
            return content

    def get_access_token_from_wx(self):
        """
        从微信服务器获取accessToken.
        相当于强制刷新缓存中的accessToken
        :return:
        """
        try:
            url = self.GET_ACCESS_TOKEN_URL.format(self.appid, WECHAT_CONF[self.appid]['appsecret'])
        except Exception as e:
            print('获取配置失败: %s' % e)
            return None

        r = requests.get(url)
        if r.status_code == 200:
            result = r.json()
            if 'access_token' in result:
                self.access_token = result['access_token']
                self._store_access_token(WX_ACCESS_TOKEN_STORE_WAY)
                return self.access_token
            else:
                print('获取accessToken失败，错误信息:%s' % result)
                return None
        else:
            return None

    def get_access_token(self):
        """
        从本地获取accessToken,如果没有则从微信服务器获取.
        :return:
        """
        return self._get_local_access_token(WX_ACCESS_TOKEN_STORE_WAY) or self.get_access_token_from_wx()

    def join_url(self, url):
        """
        将access_token拼接到url中
        :param url:
        :return:
        """
        if not self.access_token:
            raise NotAccessTokenException
        if url.find('?') >= 0:
           return url + '&access_token=' + self.access_token
        else:
            return url + '?access_token=' + self.access_token

    def post(self, url, json=None, file=None, data=None, expire_retry=True):
        """
        post数据到微信服务器
        :param message: Dictionary
        :param json:
        :param file:
        :param data:
        :param expire_retry: accessToken过期重试
        :return:   Dictionary
        """
        try:
            joined_url = self.join_url(url)
        except NotAccessTokenException:
            print('access token is empty')
            return None

        r = requests.post(joined_url, data=data, json=json, files=file)
        if r.status_code == 200:
            try:
                result = r.json()
            except:
                result = None
            if result:
                if result.get('errcode') in (42001,40001,40014) and expire_retry:
                    self.get_access_token_from_wx()
                    return self.post(url, json=json, file=file, data=data, expire_retry=False)

                print('response:%s' % result)
                return result
            else:
                print('response content:%s' % r.content)
                return r.content
        else:
            print('status_code: %d' % r.status_code)
            return None

    def get(self, url, json=None, data=None, expire_retry=True, join_access_token=True):
        """
        get请求
        :param url:
        :param json:
        :param data:
        :param expire_retry:
        :return:
        """
        joined_url = url
        if join_access_token:
            try:
                joined_url = self.join_url(url)
            except NotAccessTokenException:
                print('access token is empty')
                return None

        r = requests.get(joined_url, data=data, json=json)
        if r.status_code == 200:
            result = r.json()
            if result.get('errcode') in (42001,40001,40014) and expire_retry:
                self.get_access_token_from_wx()
                return self.get(url, json=json, data=data, expire_retry=False)

            print('response:%s' % result)
            return result
        else:
            print('status_code: %d' % r.status_code)
            return None

if __name__ == '__main__':
    baseService = WxBaseService('wxbd77bc158b32c535')
    print(baseService.get_access_token_from_wx())