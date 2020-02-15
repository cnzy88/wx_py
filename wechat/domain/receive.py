#coding: utf-8
import xml.etree.ElementTree as ET

class WxMessage(object):
    """
    微信消息模型
    """

    def __init__(self, appid=None, from_user=None, to_user=None, msg_type=None, create_time=None, event=None, content=None, event_key=None):
        """
        :param appid:  公众号id
        :param from_user:  发送者
        :param to_user:    接收者
        :param msg_type:    消息类型
        :param create_time:    消息时间戳
        :param event:      事件
        :param content:    内容
        :param event_key:    事件附带的参数
        """
        self.appid = appid
        self.from_user = from_user
        self.to_user = to_user
        self.msg_type = msg_type
        self.create_time = create_time
        self.event = event
        self.content = content
        self.event_key = event_key

def handle_xml_data(xml_data, appid):
    """
    处理微信传过来的xml数据
    :param xml_data: 原始数据
    :param appid:    公众号id
    :return:   WxMessage
    """
    root = ET.fromstring(xml_data)
    from_user = root.findtext(".//FromUserName")
    to_user = root.findtext(".//ToUserName")
    create_time = root.findtext(".//CreateTime")
    msg_type = root.findtext(".//MsgType")
    event = root.findtext(".//Event")
    content = root.findtext(".//Content")
    event_key = root.findtext(".//EventKey")

    return WxMessage(appid=appid, from_user=from_user, to_user=to_user, msg_type=msg_type, event=event, content=content,
                     create_time=create_time, event_key=event_key)
