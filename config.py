#coding: utf-8

#微信access_token在本地存储方式:  1: redis存储  2: 文件存储
WX_ACCESS_TOKEN_STORE_WAY = 2

#微信公众号配置
WECHAT_CONF = {
    #测试服务号
    'wxbd77bc158b32c535': {
        "appsecret": "",
        "token": "",
        "pays": {
            "notify_url": "",
            "mch_id": "",
            "body": "",
            "trade_type": "",
        },
        "pay_key": ""
    }
}