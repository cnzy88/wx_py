import time

class TextReply(object):
    def __init__(self, toUserName, content, fromUserName=None):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = content

    def send(self):
        XmlForm = """
          <xml>
          <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
          <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
          <CreateTime>{CreateTime}</CreateTime>
          <MsgType><![CDATA[text]]></MsgType>
          <Content><![CDATA[{Content}]]></Content>
          </xml>
        """
        return XmlForm.format(**self.__dict)


class ImageReply(object):
    def __init__(self, toUserName, mediaId, fromUserName=None):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MediaId'] = mediaId

    def send(self):
        XmlForm = """
          <xml>
          <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
          <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
          <CreateTime>{CreateTime}</CreateTime>
          <MsgType><![CDATA[image]]></MsgType>
          <Image>
          <MediaId><![CDATA[{MediaId}]]></MediaId>
          </Image>
            </xml>
        """
        return XmlForm.format(**self.__dict)
