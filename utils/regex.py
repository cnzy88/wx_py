#coding: utf-8
import re

class RegexHelp(object):

    @staticmethod
    def match_number(source):
        """
        匹配字符串中的数字
        :param source: 原始数字
        :return: list  匹配到的数字的列表
        """
        return re.findall('\d+',source)

    @staticmethod
    def match(source, regex):
        """
        自定义规则匹配
        :param source:  原始字符串
        :param regex:   匹配规则
        :return:  list  匹配到的数据的列表
        """
        return re.findall(regex, source)

    @staticmethod
    def match_one(source, regex):
        """
        自定义规则匹配，只返回匹配到的第一个字符串
        :param source:
        :param regex:
        :return:  String
        """
        data = re.findall(regex, source)
        if not data:
            return None
        return data[0]

if __name__ == '__main__':
    source = "fdsf表格示例.2019-12文件名"
    print RegexHelp.match_one(source, "\d+-\d+")