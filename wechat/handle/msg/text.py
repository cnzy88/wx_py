#coding: utf-8
from wechat.domain.reply import *
from wechat.service.kefu import WxKefuService


def handle(wx_message):
    """
    接收到文字进行处理
    :param wx_message: WxMessage
    :return: String
    """
    result = 'success'
    content = wx_message.content
    from_user = wx_message.from_user
    if content == '测试':
        # return TextReply(from_user, '测试').send()
        kefu_service = WxKefuService(wx_message.appid)
        kefu_service.send_text_message(from_user, '这是一个测试')

    return result