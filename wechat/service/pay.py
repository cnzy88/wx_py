#coding: utf-8
import hashlib
import string
import random
import time
from wechat.service.base import WxBaseService
from wechat.exception import WeixinPayError
from utils.xml_help import XmlOperate
from config import WECHAT_CONF
from utils.common import get_local_ip

class WxPayService(WxBaseService):
    """
        统一下单用法示例
        appid = ''
        pay_service = WxPayService(appid)
        data = WECHAT_CONF[appid]['pay']
        data['openid'] = ""
        data['total_fee'] = 100
        pay_service.unified_order(**data)
    """

    #统一下单
    UNIFIED_ORDER_URL = "https://api.mch.weixin.qq.com/pay/unifiedorder"

    def __init__(self, appid):
        super(WxPayService, self).__init__(appid)
        self.pay_key = WECHAT_CONF[appid]['pay_key']

    def _generate_wx_pay_sign(self, raw):
        """
        生成微信支付签名
        :param raw:  Dictionary
        :return:  String
        """
        raw = [(k, str(raw[k]) if isinstance(raw[k], (int, float)) else raw[k]) for k in sorted(raw.keys())]
        s = "&".join("=".join(kv) for kv in raw if kv[1])
        s += "&key={0}".format(self.pay_key)
        return hashlib.md5(s.encode("utf8")).hexdigest().upper()

    def _generate_nonce_str(self, length=32):
        """
        生成随机字符串
        :param length:  字符串长度
        :return:  String
        """
        char = string.ascii_letters + string.digits
        return "".join(random.choice(char) for _ in range(length))

    def unified_order(self, **data):
        """
        下单
        :param openid:  用户id
        :param trade_type:  交易类型  (1)JSAPI -JSAPI支付   (2)NATIVE -Native支付  (3)APP -APP支付
        :param total_fee:  订单总金额，单位为分
        :param spbill_create_ip   用户的客户端IP
        :param appid:  公众账号ID
        :param openid:  用户id
        :param mch_id:  微信支付分配的商户号
        :param nonce_str:  随机字符串，长度要求在32位以内
        :param sign:  签名
        :param body:  商品描述
        :param out_trade_no:  商户订单号
        :param total_fee:  订单总金额，单位为分
        :param notify_url   支付结果通知回调地址
        :param trade_type:  交易类型  (1)JSAPI -JSAPI支付   (2)NATIVE -Native支付  (3)APP -APP支付
        :param spbill_create_ip   用户的客户端IP
        :return: Dictionary e.g
            {
                'trade_type': u 'JSAPI',
                'prepay_id': u '',
                'nonce_str': u '',
                'return_code': u 'SUCCESS',
                'return_msg': u 'OK',
                'sign': u '',
                'mch_id': u '',
                'appid': u '',
                'result_code': u 'SUCCESS'
            }
        """

        if "total_fee" not in data:
            raise WeixinPayError("缺少统一支付接口必填参数total_fee")
        if data["trade_type"] == "JSAPI" and "openid" not in data:
            raise WeixinPayError("trade_type为JSAPI时，openid为必填参数")

        if "spbill_create_ip" not in data:
            data['spbill_create_ip'] = get_local_ip()

        data['appid'] = self.appid
        data['out_trade_no'] = self._generate_nonce_str()
        #todo: 保存订单号到数据库
        data['nonce_str'] = self._generate_nonce_str()
        data['sign'] = self._generate_wx_pay_sign(data)

        data = XmlOperate.dict_to_xml(data).encode('utf-8')
        print('wx pay request data:%s' % data)
        result = self.post(self.UNIFIED_ORDER_URL, data=data)
        if result:
            r = XmlOperate.xml_to_dict(result)
            if r.get('result_code') == 'SUCCESS':
                return r
            else:
                print('wx pay failed: %s' % r)
                return None
        else:
            return None

    def generate_js_api_data(self, **kwargs):
        """
        生成给JavaScript调用的数据
        :param kwargs:
            trade_type:
            prepay_id:
            nonce_str:
            sign:
            mch_id:
            appid:
        :return: 生成微信JS接口支付所需的信息
        """
        if not kwargs:
            return None
        package = "prepay_id={0}".format(kwargs["prepay_id"])
        timestamp = int(time.time())
        nonce_str = kwargs["nonce_str"]
        sign = kwargs["sign"]
        return dict(package=package, appId=self.appid,
                    timeStamp=timestamp, nonceStr=nonce_str, sign=sign)

    def check(self, kwargs):
        """
        检查微信异步回调返回的签名是否正确
        :param kwargs:
        :return: Boolean
        """
        sign = kwargs.pop("sign")
        return sign == self._generate_wx_pay_sign(kwargs)

    def reply(self, msg, ok=True):
        """
        对微信异步回调进行回复
        :param msg:
        :param ok:
        :return:
        """
        code = "SUCCESS" if ok else "FAIL"
        return XmlOperate.dict_to_xml(dict(return_code=code, return_msg=msg))

if __name__ == '__main__':
    appid = 'wx6fbc9936bb2b5416'
    pay_service = WxPayService(appid)
    data = WECHAT_CONF[appid]['pay']
    data['openid'] = "oBDdnwjeF5LcLCNjefX5n5TG8Blk"
    data['total_fee'] = 100
    print(pay_service.unified_order(**data))
