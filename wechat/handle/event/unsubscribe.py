#coding: utf-8
from wechat.service.kefu import WxKefuService


def handle(wx_message):
    """
    取关处理
    :param wx_message: WxMessage
    :return: String
    """
    result = 'success'
    print('取关详情:%s' % wx_message)

    return result