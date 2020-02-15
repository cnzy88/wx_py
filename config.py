#coding: utf-8

#微信access_token在本地存储方式:  1: redis存储  2: 文件存储。如果没有redis,可以选择文件存储方式。如果是正式的服务，推荐用redis存储方式。
# 毕竟redis读写比文件要快很多。
WX_ACCESS_TOKEN_STORE_WAY = 2

#微信公众号配置
WECHAT_CONF = {
    #白熊规划服务号
    'wx6fbc9936bb2b5416': {
        "appsecret":"77dcc292643a36936f6c7fae71e7f26f",
        "token":"RocketAi",
        "pay": {
            "notify_url": "http://cnzy.easy.echosite.cn/wechat_portal/pay/notify",
            "mch_id": "1540760681",
            "body": "1v1支付",
            "trade_type": "JSAPI",
        },
        "pay_key": "a7a3407396eaa2bc940fdd66ffe5d725"
    },
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