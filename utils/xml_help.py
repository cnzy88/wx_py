#coding: utf-8
from bs4 import BeautifulSoup

class XmlOperate(object):

    @staticmethod
    def xml_to_dict(xml):
        """
        将微信支付交互返回的 XML 格式数据转化为 Python Dict 对象

        :param xml: 原始 XML 格式数据
        :return: dict 对象
        """

        soup = BeautifulSoup(xml, features='xml')
        xml = soup.find('xml')
        if not xml:
            return {}

        data = dict([(item.name, item.text) for item in xml.find_all()])
        return data

    @staticmethod
    def dict_to_xml(data):
        """
         将 dict 对象转换成微信支付交互所需的 XML 格式数据

         :param data: dict 对象
         :return: xml 格式数据
         """
        xml = []
        for k in sorted(data.keys()):
            v = data.get(k)
            if k == 'detail' and not v.startswith('<![CDATA['):
                v = '<![CDATA[{}]]>'.format(v)
            xml.append('<{key}>{value}</{key}>'.format(key=k, value=v))
        return '<xml>{}</xml>'.format(''.join(xml))


if __name__ == '__main__':
    s = b'<xml><return_code><![CDATA[SUCCESS]]></return_code>\n<return_msg><![CDATA[OK]]></return_msg>\n<appid><![CDATA[wx6fbc9936bb2b5416]]></appid>\n<mch_id><![CDATA[1540760681]]></mch_id>\n<nonce_str><![CDATA[xDCFXRIIpYofbb45]]></nonce_str>\n<sign><![CDATA[16C8727FAA8BD89DBAB9315C010D64C8]]></sign>\n<result_code><![CDATA[SUCCESS]]></result_code>\n<prepay_id><![CDATA[wx15134727367117b8018d12481423507500]]></prepay_id>\n<trade_type><![CDATA[JSAPI]]></trade_type>\n</xml>'
    XmlOperate.xml_to_dict(s)