#coding: utf-8
import json
from base import WxBaseService
from utils.common import generate_random_str
from config import WECHAT_CONF

class WxLoginService(WxBaseService):

    #获取微信认证
    GET_AUTHORIZE_URL = "https://open.weixin.qq.com/connect/oauth2/authorize?" \
                        "appid={0}&redirect_uri={1}&response_type=code&scope={2}&state={3}#wechat_redirect"
    #获取微信登录的accessToken
    GET_LOGIN_ACCESS_TOKEN_URL = "https://api.weixin.qq.com/sns/oauth2/access_token?" \
                                 "appid={0}&secret={1}&code={2}&grant_type=authorization_code"
    #获取用户信息
    GET_USER_INFO_URL = "https://api.weixin.qq.com/sns/userinfo?access_token={0}&openid={1}&lang=zh_CN"

    def __init__(self, appid):
        super(WxLoginService, self).__init__(appid)

    def get_login_access_token(self, code):
        """
        获取登录accessToken.此accessToken是给前端用的，跟调微信接口中的accessToken不同。
        :param code:
        :return: example:
           {
            "openid": "oBDdnwjeF5LcLCNjefX5n5TG8Blk",
            "access_token": "30_lfBogglcUQnkWVjGARjkhNh1SzYzMA8zsH2sJAm53DsbkWvVQ4TqcMyjImYJhBgiYf-EcKQGDRjmX-2AXsY3xw",
            "unionid": "ooUBZwfmJZIak8MNhYlgng3Ew3Tk",
            "expires_in": 7200,
            "scope": "snsapi_userinfo",
            "refresh_token": "30_dnmD1EkxW3YzNZ_jGpIZoXlbIS7PL7owPTAwjfmTh5e6mryQkSGDw_yhLZuhsth80MlN7_Va8m7XhZ9NtXPHQA"
            }
        """
        url = self.GET_LOGIN_ACCESS_TOKEN_URL.format(self.appid, WECHAT_CONF[self.appid]['appsecret'], code)
        result = self.get(url, join_access_token=False)
        if result:
            if result.get('errcode'):
                print('get login access token failed: %s' % result)
                return None
            else:
                return result
        else:
            return None


    def get_authorize_url(self, redirect_uri, scope="snsapi_base", state=None):
        """生成微信授权url
        :param redirect_uri:   用户授权成功后跳转的地址(也就是页面的地址)
        :param scope: snsapi_base or snsapi_userinfo
        :param state:
        :return:  url:  String
        """
        if not state:
            state = generate_random_str(8)

        import urllib
        return self.GET_AUTHORIZE_URL.format(self.appid, urllib.quote_plus(redirect_uri), scope, state)

    def get_user_info(self, access_token, openid):
        """
        获取用户信息
        :param access_token:  微信授权时由code换取的accessToken
        :param openid:        用户在此公众号下的id
        :return:   e.g:
            {
                "province": "广东",
                "openid": "oBDdnwjeF5LcLCNjefX5n5TG8Blk",
                "headimgurl": "http://thirdwx.qlogo.cn/mmopen/vi_32/DYAIOgq83epA6Ltra5NXO081TVdqWBK7LQaYGTT0cZzbNHUNEkJsxyrhDE3iaCVKA7TskoC2xQd9IRd1Giauh5YA/132",
                "language": "zh_CN",
                "city": "珠海",
                "country": "中国",
                "sex": 1,
                "unionid": "ooUBZwfmJZIak8MNhYlgng3Ew3Tk",
                "privilege": [],
                "nickname": "黄炜"
            }
        """
        result = self.get(self.GET_USER_INFO_URL.format(access_token, openid), join_access_token=False)
        if result:
            errcode = result.get('errcode')
            if errcode:
                print('get user info failed: %s' % result)
                return None
            else:
                s = json.dumps(result, ensure_ascii=False).encode('iso-8859-1').decode('utf8')
                return json.loads(s)
        else:
            return None

if __name__ == '__main__':
    from utils.common import change_dic_to_json_str
    login_service = WxLoginService('wx6fbc9936bb2b5416')
    # print login_service.get_authorize_url('https://group.rocketai.cn/login/xxx', scope="snsapi_userinfo")
    # print login_service.get_login_access_token('011gQto91Y10KL1jBWr918Auo91gQtoy')
    result = login_service.get_user_info('30_KaHYT7376QfK9TOwYfWoRZL_7k0RiBnHKwgeoan0TmX5qZ7L9h0yx6WkrDL1Firg85lkc5AORaPTH0ASY08vJA', '123')
    print change_dic_to_json_str(result)
