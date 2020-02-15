#coding: utf-8
import json
from base import WxBaseService

class WxKefuService(WxBaseService):

    # 发送客服消息的地址
    SEND_KEFU_MESSAGE_URL = 'https://api.weixin.qq.com/cgi-bin/message/custom/send'

    def __init__(self, appid):
        super(WxKefuService, self).__init__(appid)

    def send_text_message(self, touser, content):
        """
        发送文字消息
        :param touser:
        :param content:
        :return:
        """
        message = {}
        message['touser'] = touser
        message['msgtype'] = 'text'
        message['text'] = {
            'content': content
        }

        message = json.dumps(message, ensure_ascii=False).encode('utf-8')
        result = self.post(self.SEND_KEFU_MESSAGE_URL, data=message)
        return result and result.get('errcode') == 0

    def send_image_message(self, touser, media_id):
        """
        发送图片消息
        :param touser:
        :param media_id:
        :return:
        """
        message = {}
        message['touser'] = touser
        message['msgtype'] = 'image'
        message['image'] = {
            'media_id': media_id
        }
        result = self.post(self.SEND_KEFU_MESSAGE_URL, json=message)
        return result and result.get('errcode') == 0

if __name__ == '__main__':
    kefu_service = WxKefuService(appid='wxbd77bc158b32c535')
    print kefu_service.send_image_message('oLbr-wVN2vIOOWfFC7CgQBtIb39c', 'RzDDEEU1HkeQiIAQxS17iVJRw3ttFTgKGhjeqVkY1cc')