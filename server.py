# -*- coding: utf-8 -*-
from web import app


if __name__ == '__main__':
    # 启动服务器
    app.run(host='127.0.0.1',port=3800,threaded=True, debug=True)
