# -*- coding: utf-8 -*-
import pprint
import sys
from flask import Flask
from flask import jsonify
from utils.response_help import ResponseHelp

reload(sys)
sys.setdefaultencoding('utf-8')

class MyFlask(Flask):
    def make_response(self, rv):
        if isinstance(rv, dict):
            if rv.get('code') != 0:
                print('接口返回结果可能失败: %s', rv.get('msg'))
            rv = jsonify(rv)
        return super(MyFlask, self).make_response(rv)

app = MyFlask(__name__)


@app.errorhandler(Exception)
def all_exception_handler(error):
    print("接口处理过程发生异常: %s", pprint.pformat(error))
    return ResponseHelp.failed_simplify(str(error))

from view import message,login,pay