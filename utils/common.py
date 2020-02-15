#coding: utf-8
import sys
import os
import datetime
import random
import string
from uuid import uuid1

reload(sys)
sys.setdefaultencoding('utf-8')

def count_time(func):
    """
    计算函数允许时间装饰器
    :param func:
    :return:
    """
    def int_time(*args, **kwargs):
        start_time = datetime.datetime.now()
        func(*args, **kwargs)
        over_time = datetime.datetime.now()
        total_time = over_time-start_time
        print('total time: %ss' % total_time.total_seconds())
    return int_time

def judge_os_platform():
    """
    判断当前允许程序的操作系统类型
    :return:
    """
    platform = os.name
    if platform == 'nt':
        return 'windows'
    elif platform == 'posix':
        return 'linux'
    else:
        return None

def get_dir_files(dir):
    """
    获取某个目录下的所有文件
    :param dir:
    :return:
    """
    for root, dirs, files in os.walk(dir):
        return files

def html_to_pdf(content, new_file_name):
    """
    将html转成pdf
    :return:
    """
    import pdfkit
    config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

    return pdfkit.from_string(content, new_file_name, configuration=config)

def change_dic_to_json_str(obj):
    """
    将python字典转为json字符串
    :param obj:
    :return:
    """
    import json
    if not obj:
        if isinstance(obj, dict):
            return None
        elif isinstance(obj, list):
            return []
        elif isinstance(obj, str):
            return ''
        else:
            return None
    return json.dumps(obj, ensure_ascii=False)

def str_unicode_change():
    """
    str和unicode互转
    #---decode---
    #str------>unicode
    #\xe5\xb2\-->\u5e74\u9f84

    #str<------unicode
    #----encode-------
    :return:
    """
    pass

def generate_random_str(num):
    """
    生成包含英文和数字的随机字符串
    :param num:  位数
    :return:
    """
    return ''.join(random.sample(string.ascii_letters + string.digits, num))

def get_local_ip():
    """
    获取本机ip(局域网ip)
    :return:
    """
    import socket
    myname = socket.getfqdn(socket.gethostname())
    myaddr = socket.gethostbyname(myname)
    return myaddr

def str_to_hump(text):
    """
    将python下划线的命名转为驼峰式命名
    :param text:
    :return:
    """
    arr = filter(None, text.lower().split('_'))
    res = ''
    j = 0
    for i in arr:
        if j == 0:
            res = i
        else:
            res = res + i[0].upper() + i[1:]
        j += 1
    return res


if __name__ == '__main__':
    pass