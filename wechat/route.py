#coding: utf-8
import importlib

MSG_TYPE = ['text', 'image', 'subscribe', 'unsubscribe', 'scan']

def handler_map_factory(msg_types):
    """
    Handler Map对象工厂函数
    :param msg_types:
    :return:
    """
    handler_map = {}
    handlers = importlib.import_module('wechat.handle')

    for msg_type in msg_types:
        handler_map.setdefault(msg_type, handlers.__dict__[msg_type].handle)

    return handler_map

handler_map = handler_map_factory(MSG_TYPE)

def route_handle(wx_message):
    """
    对接收到的来自微信的消息路由到对应的handle
    :param wx_message:  WxMessage
    :return:
    """
    msg_type = wx_message.msg_type
    if msg_type == 'event':
        msg_type = wx_message.event

    if msg_type in MSG_TYPE:
        return handler_map[msg_type](wx_message)
    else:
        print('Not found msg type: %s' % msg_type)
        return 'success'
