#coding: utf-8
from base import WxBaseService

class WxTemplateMsgService(WxBaseService):

    #获取模板id的di地址
    GET_TEMPALTE_MSG_ID_URL = "https://api.weixin.qq.com/cgi-bin/template/api_add_template"
    #h获取模板消息列表的地址
    GET_TEMPLATE_MSG_LIST_URL = "https://api.weixin.qq.com/cgi-bin/template/get_all_private_template"
    #发送模板消息的地址
    SEND_TEMPLATE_MSG_URL = "https://api.weixin.qq.com/cgi-bin/message/template/send"

    def __init__(self, appid):
        super(WxTemplateMsgService, self).__init__(appid)

    def get_template_id(self, template_id_short):
        """
        根据template_id_short获取模板id(暂时不清楚这个template_id_short是啥)
        :param name:
        :return:
        """
        body = {}
        body['template_id_short'] = template_id_short
        result = self.post(self.GET_TEMPALTE_MSG_ID_URL, json=body)
        print result

    def get_template_list(self):
        """
        获取模板消息列表
        :return:
        """
        result = self.get(self.GET_TEMPLATE_MSG_LIST_URL)
        return result.get('template_list') if result else None

    def send_template_msg(self, touser, template_id, data, url=None):
        """
        发送模板消息
        :param touser:       openid
        :param template_id:  模板id
        :param data:          example:
                {
                   "first": {
                       "value":"恭喜你购买成功！",
                       "color":"#173177"
                   },
                   "keyword1":{
                       "value":"巧克力",
                       "color":"#173177"
                   },
                   "keyword2": {
                       "value":"39.8元",
                       "color":"#173177"
                   },
                   "keyword3": {
                       "value":"2014年9月22日",
                       "color":"#173177"
                   },
                   "remark":{
                       "value":"欢迎再次购买！",
                       "color":"#173177"
                   }
           }
        :param url:   点击模板消息跳转url
        :return:  Boolean
        """
        body = {}
        body['touser'] = touser
        body['template_id'] = template_id
        body['data'] = data
        body['url'] = url

        result = self.post(self.SEND_TEMPLATE_MSG_URL, json=body)
        return result and result.get('errcode') == 0


if __name__ == '__main__':
    template_service = WxTemplateMsgService('wx6fbc9936bb2b5416')
    data = {
        'first': {
            'value': '点击详情参与抽奖！',
            'color': '#3385FF'  # 蓝色
        },
        'keyword1': {
            'value': '您的好友已购买新型冠状病毒保障！',
            'color': '#5F9EA0'
        },
        'keyword2': {
            'value': '测试',
            'color': '#5F9EA0'
        },
        'remark': {
            'value': '点击查看详情参与抽奖',
            'color': '#990033'
        }
    }
    # print template_service.send_template_msg('oBDdnwjeF5LcLCNjefX5n5TG8Blk', '5X2iCrQ_V7sdBxdAHweBKa0mC8G3JsRGOkt8G0NdhPw', data)
    print template_service.get_template_list()
