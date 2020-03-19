#coding: utf-8

#微信access_token在本地存储方式:  1: redis存储  2: 文件存储。如果没有redis,可以选择文件存储方式。如果是正式的服务，推荐用redis存储方式。
# 毕竟redis读写比文件要快很多。
WX_ACCESS_TOKEN_STORE_WAY = 2

#微信公众号配置
WECHAT_CONF = {
    #测试服务号
    'wxbd77bc158b32c535': {
        "appsecret":"203c9565ef21b39ecabe6698d7537546",
        "token":"cnzy88",
        "pays": {
            "notify_url": "",
            "mch_id": "",
            "body": "",
            "trade_type": "",
        },
        "pay_key": ""
    }
}