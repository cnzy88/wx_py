#coding: utf-8
from flask import request
from web import app
from wechat.service.login import WxLoginService
from utils.response_help import ResponseHelp

@app.route('/wechat_portal/get_access_token', methods=['GET'])
def get_access_token():
    appid = request.args.get('appid')
    code = request.args.get('code')
    if not appid:
        return ResponseHelp.failed_simplify('appid could not empty.')
    if not code:
        return ResponseHelp.failed_simplify('could could not empty.')

    login_service = WxLoginService(appid)
    result = login_service.get_login_access_token(code)
    if result:
        return ResponseHelp.success(result)
    else:
        return ResponseHelp.failed_simplify('get access token faild.')

