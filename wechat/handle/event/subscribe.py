#coding: utf-8
from wechat.domain.reply import *
from wechat.service.kefu import WxKefuService


def handle(wx_message):
    """
    关注处理
    :param wx_message: WxMessage
    :return: String
    """
    result = 'success'
    from_user = wx_message.from_user

    kefu_service = WxKefuService(wx_message.appid)
    kefu_service.send_text_message(from_user, '欢迎您的到来!')

    return result