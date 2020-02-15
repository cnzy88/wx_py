#coding: utf-8
import hashlib
from flask import request
from web import app
from config import WECHAT_CONF
from wechat.route import route_handle
from utils.xml_help import XmlOperate
from wechat.model.wx_message import WxMessage


@app.route('/wechat_portal/message/<appid>', methods=['GET'])
def get(appid):
    try:
        token = WECHAT_CONF[appid]['token']
    except:
        print('app config is not exist.')
        return ''

    data = request.args
    if len(data) == 0:
        print('data from wechat is empty.')
        return ''

    signature = data.get('signature')
    timestamp = data.get('timestamp')
    nonce = data.get('nonce')
    echostr = data.get('echostr')

    list = [token, timestamp, nonce]
    list.sort()
    sha1 = hashlib.sha1()
    map(sha1.update, list)
    hashcode = sha1.hexdigest()
    if hashcode == signature:
        print('signature from remote check success.')
        return echostr
    else:
        print('signature from remote check fail.')
        return ''

@app.route('/wechat_portal/message/<appid>', methods=['POST'])
def post(appid):
    """
    微信推送消息统一入口,后续再经由route_handle分发到对应的handler
    :param appid:
    :return:
    """
    xml_data = request.data
    print('xml data from wechat: %s' % xml_data)

    data = XmlOperate.xml_to_dict(xml_data)
    data['appid'] = appid
    wx_message = WxMessage(**data)
    print('wx_message: %s' % wx_message)

    return route_handle(wx_message)
