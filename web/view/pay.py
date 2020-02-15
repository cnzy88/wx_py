#coding: utf-8
from flask import request
from web import app
from wechat.service.pay import WxPayService
from utils.xml_help import XmlOperate


@app.route('/wechat_portal/pay/notify', methods=['GET'])
def pay_notify():
    """
    微信异步通知
    """
    data = XmlOperate.xml_to_dict(request.data)
    print('pay notify data: %s' % data)
    pay_service = WxPayService(data.get('appid'))
    if not pay_service.check(data):
        return pay_service.reply("sign check faild", False)

    #todo:处理业务逻辑

    return pay_service.reply("OK", True)

