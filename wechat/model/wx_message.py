#coding: utf-8
import xml.etree.ElementTree as ET

class WxMessage(object):
    """
    微信消息模型
    """

    def __init__(self, appid=None, FromUserName=None, ToUserName=None, MsgType=None, CreateTime=None, Event=None, Content=None, EventKey=None):
        """
        接收参数命名保持跟微信一致
        :param appid:  公众号id
        :param FromUserName:  发送者
        :param ToUserName:    接收者
        :param MsgType:    消息类型
        :param CreateTime:    消息时间戳
        :param Event:      事件
        :param Content:    内容
        :param EventKey:    事件附带的参数
        """
        self.appid = appid
        self.from_user = FromUserName
        self.to_user = ToUserName
        self.msg_type = MsgType
        self.create_time = CreateTime
        self.event = Event
        self.content = Content
        self.event_key = EventKey

    def __repr__(self):
        return ', '.join('%s:%s' % (k, v) for (k, v) in self.__dict__.items())
