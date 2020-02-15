#coding: utf-8
import hashlib
from flask import request
from web import app
from config import WECHAT_CONF
from wechat.route import route_handle
from wechat.domain.receive import handle_xml_data


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
    xml_data = request.data
    print('xml data from wechat: %s' % xml_data)

    wx_message = handle_xml_data(xml_data, appid)

    return route_handle(wx_message)
