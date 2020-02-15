#coding: utf-8
from wechat.handle import *

def route_handle(wx_message):
    """
    对接收到的来自微信的消息路由到对应的handle
    :param wx_message:  WxMessage
    :return:
    """
    msg_type = wx_message.msg_type
    if msg_type == 'text':
        return text.handle(wx_message)
    elif msg_type == 'event':
        event = wx_message.event
        if event == 'subscribe':
            return subscribe.handle(wx_message)
        elif event == 'scan':
            return scan.handle(wx_message)

    return 'success'
